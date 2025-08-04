import pytest
from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts, User
from backend.application.crud.workouts import get_all_workouts, get_workout_with_sections_and_routines
from backend.tests.test_utils import insert_sample_entire_workout
from backend.application.crud.user import create_user
from backend.application.schemas import UserCreate
from backend.application.utilities.security import verify_password

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
    db.close()"""
    
def test_create_user():
    db = SessionLocal()
    
    test_user = UserCreate(Email="test@example.com", Password="Orange23")
        
    create_test_user = create_user(db, test_user)
    
    assert create_test_user.Email == test_user.Email
    assert verify_password("Orange23", create_test_user.HashedPassword)
    
    db.delete(create_test_user)
    db.commit()
    db.close()
        

        

    
    
    
    
