#tests all the crud functions

import pytest
from unittest.mock import MagicMock
from fastapi import status, HTTPException
from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts, User, UserWorkoutRequest
from backend.application.crud.workouts import get_all_workouts, get_workout_with_sections_and_routines
from backend.tests.test_utils import insert_sample_entire_workout, insert_sample_user
from backend.application.crud.user import create_user, get_user_email_and_active_status, update_user_password
from backend.application.crud.user_request import create_workout_request
from backend.application.schemas import UserCreate, UserPasswordChange, UserWorkoutRequestCreate, RequestTypeEnum
from backend.application.utilities.security import get_password_hash, verify_password

"""#insert workout sample data into the workouts table in the test db
def insert_test_workout(db):
    workout = workouts(Name="Test 1", Description="Test Description 1")
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

#checks an inserted workout is present when the list of all workouts is shown
def test_workout_retrieval():
    db = SessionLocal()
    
    inserted = insert_test_workout(db)
    results = get_all_workouts(db)

    names = []
    for w in results:
        names.append(w.Name)
    assert inserted.Name in names
    
    db.delete(inserted)
    db.commit()
    db.close()
"""
#inserts entire sample workout and check its been entered correctly and retrieved correctly
def test_workout_with_sections_and_routines():
    db = SessionLocal()
    workout, section, routine = insert_sample_entire_workout(db)
        
    result = get_workout_with_sections_and_routines(db, "Test Workout")
        
    assert result is not None
    assert result.Name == workout.Name
    assert len(result.Sections) == 1
    assert result.Sections[0].SectionName == section.SectionName # use 0 as result.Sections is a list
    assert len(result.Sections[0].Routines) == 1
    assert result.Sections[0].Routines[0].Name == routine.Name
    
    db.delete(routine)
    db.delete(section)
    db.delete(workout)
    db.commit()
    db.close()
 
#tests the creation of a new user and checks its email and password is correct    
def test_create_user():
    db = SessionLocal()
    
    test_user = UserCreate(Email="test1@example.com", Password="Orange23")
        
    create_test_user = create_user(db, test_user)
    
    assert create_test_user.Email == test_user.Email
    assert verify_password("Orange23", create_test_user.HashedPassword)
    
    db.delete(create_test_user)
    db.commit()
    db.close()

#tests that the users details e.g. email and active status is retrieved correctly    
def test_retrieve_user_details():
    db = SessionLocal()
    
    user = insert_sample_user(db)
    result = get_user_email_and_active_status(user)
    
    assert result.Email == user.Email
    assert result.IsActive == user.IsActive
    
    db.delete(user)
    db.commit()
    db.close()

#tests the user updating their password correctly using mocking    
def test_update_user_password_success():
    original_test_password = "oldpassword1"
    hashed_password = get_password_hash(original_test_password)
    
    mock_user = User()
    mock_user.HashedPassword = hashed_password
    mock_db = MagicMock()
    
    user_test_input = UserPasswordChange(current_password="oldpassword1", new_password="newpassword2")
    response = update_user_password(db=mock_db, user_input=user_test_input, current_user=mock_user)
    
    assert verify_password("newpassword2", mock_user.HashedPassword)
    mock_db.commit.assert_called_once()
    
    assert response == {"message": "Password updated successfully"}

#tests the correct errors are raised when the wrong password is entered to update the user's password    
def test_update_user_password_failure():
    hashed_password = get_password_hash("correctpassword")
    mock_user = User()
    mock_user.HashedPassword = hashed_password
    
    mock_db = MagicMock()
    
    user_test_input = UserPasswordChange(current_password="wrongpassword", new_password="Bluesky1")
    
    with pytest.raises(HTTPException) as exc_info:
        update_user_password(db=mock_db, user_input=user_test_input, current_user=mock_user)
        
    assert exc_info.value.status_code == status.HTTP_403_FORBIDDEN

#tests the user requesting for a specific request. This is the successful test.    
def test_create_workout_request_success():
    db = SessionLocal()

    user = User(Email="test_success_user2@example.com", HashedPassword="test", IsActive=True)
    db.add(user)
    db.commit()
    db.refresh(user)

    workout = workouts(Name="Everyday movement Workout", Description="Test")
    db.add(workout)
    db.commit()
    db.refresh(workout)

    req = UserWorkoutRequestCreate(request_type=RequestTypeEnum.new_workout)

    result = create_workout_request(db, user_id=user.ID, request=req)

    assert result.Name == "Everyday movement Workout"

    db.query(UserWorkoutRequest).filter(UserWorkoutRequest.UserID == user.ID).delete()
    db.query(workouts).filter(workouts.ID == workout.ID).delete()
    db.query(User).filter(User.ID == user.ID).delete()
    db.commit()
    db.close()

#tests the correct error is raised when the wrong user request is made
def test_create_workout_request_failure():
    db = MagicMock()
    
    db.query().filter().first.return_value = None

    req = UserWorkoutRequestCreate(request_type=RequestTypeEnum.new_workout)

    with pytest.raises(HTTPException) as exc:
        create_workout_request(db, user_id=123, request=req)

    assert exc.value.status_code == 404
