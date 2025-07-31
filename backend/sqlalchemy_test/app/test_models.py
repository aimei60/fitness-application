"""
Tests database models for correct insertion, retrieval, and integrity enforcement.

Covers:
- Successful creation and deletion of workout programs, sections, routines, users, profiles, and requests.
- Handling of invalid data insertions (e.g. missing required fields, invalid foreign keys).
- Ensures database constraints and relationships are correctly enforced.
"""

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy_test.app.test_database import Base, engine, SessionLocal
from backend.application.models import workouts, workout_sections, workoutRoutine, User, UserWorkoutRequest, UserProfile

def test_data_insertion_retrieval_workouts():
    session = SessionLocal()
    
    new_workout = workouts(
        Name="Test Workout",
        Description="This is a test workout"
    )
    
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)
    
    assert new_workout.ID is not None
    assert new_workout.Name == "Test Workout"
    assert new_workout.Description == "This is a test workout"
    
    session.delete(new_workout)
    session.commit()
    session.close()
    
def test_insert_invalid_workout_name():
    session = SessionLocal()
    
    bad_workout = workouts(
        Name=None,
        Description="Test"
    )
    
    session.add(bad_workout)
    
    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
    session.close()
    
def test_data_insertion_retrieval_workouts_sections():
    session = SessionLocal()
    
    new_workout = workouts(
        Name="Temporary Workout",
        Description="Temporary workout for section test"
    )
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)
    
    new_workout_section = workout_sections(
        WOID=new_workout.ID,
        SectionName="Test warm up",
        SectionOrder=4
    )
    
    session.add(new_workout_section)
    session.commit()
    session.refresh(new_workout_section)
    
    assert new_workout_section.ID is not None
    assert new_workout_section.WOID == new_workout.ID #tests valid foreign key insertion
    assert new_workout_section.SectionName == "Test warm up"
    assert new_workout_section.SectionOrder == 4
    
    session.delete(new_workout_section)
    session.delete(new_workout)
    session.commit()
    session.close()
    
def test_insert_invalid_workout_section_name():
    session = SessionLocal()
    
    new_workout = workouts(
        Name="Temporary Workout",
        Description="Temporary workout for section test"
    )
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)
    
    bad_workout_section = workout_sections(
        WOID=new_workout.ID,
        SectionName=None,
        SectionOrder=4
    )
    
    session.add(bad_workout_section)
    
    with pytest.raises(IntegrityError):
        session.commit()
        
    session.rollback()
    session.delete(new_workout)
    session.commit()
    session.close()
    
def test_insert_invalid_foreign_key_workout_section():
    session = SessionLocal()
    
    bad_workout_section = workout_sections(
        WOID=9999,
        SectionName="Bad Section",
        SectionOrder=1
    )
    
    session.add(bad_workout_section)
    
    with pytest.raises(IntegrityError):
        session.commit()
        
    session.rollback()
    session.close()
    
def test_data_insertion_retrieval_workout_routines():
    session = SessionLocal()
    
    new_workout = workouts(
        Name="Temporary Workout",
        Description="Temporary workout for section test"
    )
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)
    
    new_workout_section = workout_sections(
        WOID=new_workout.ID,
        SectionName="Test warm up",
        SectionOrder=2
    )
    
    session.add(new_workout_section)
    session.commit()
    session.refresh(new_workout_section)
    
    new_workout_routine = workoutRoutine(
        SectionID=new_workout_section.ID,
        Name="Test Arm Circles",
        RepsDuration="Test Duration",
        RoutineDescription="Test Description",
        ExerciseOrder=5
    )
    
    session.add(new_workout_routine)
    session.commit()
    session.refresh(new_workout_routine)
    
    assert new_workout_routine.ID is not None
    assert new_workout_routine.SectionID == new_workout_section.ID #tests valid foreign key insertion
    assert new_workout_routine.Name == "Test Arm Circles"
    assert new_workout_routine.RepsDuration == "Test Duration"
    assert new_workout_routine.RoutineDescription == "Test Description"
    assert new_workout_routine.ExerciseOrder == 5
    
    session.delete(new_workout_routine)
    session.delete(new_workout_section)
    session.delete(new_workout)
    session.commit()
    session.close()
    
def test_insert_invalid_workout_routine_name():
    session = SessionLocal()
    
    new_workout = workouts(
        Name="Temporary Workout",
        Description="Temporary workout for section test"
    )
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)
    
    new_workout_section = workout_sections(
        WOID=new_workout.ID,
        SectionName="Test warm up",
        SectionOrder=2
    )
    
    session.add(new_workout_section)
    session.commit()
    session.refresh(new_workout_section)   
    
    bad_workout_routine = workoutRoutine(
        SectionID=new_workout_section.ID,
        Name=None,
        RepsDuration="Test Duration",
        RoutineDescription="Test Description",
        ExerciseOrder=5
    )
    
    session.add(bad_workout_routine)
    
    with pytest.raises(IntegrityError):
        session.commit()
        
    session.rollback()
    session.delete(new_workout_section)
    session.delete(new_workout)
    session.commit()
    session.close()
    
def test_insert_invalid_foreign_key_workout_routine():
    session = SessionLocal()
    
    bad_workout_routine = workoutRoutine(
        SectionID=9999,
        Name="Bad Routine",
        RepsDuration="Test Duration",
        RoutineDescription="Test Description",
        ExerciseOrder=5
    )
    
    session.add(bad_workout_routine)
    
    with pytest.raises(IntegrityError):
        session.commit()
        
    session.rollback()
    session.close()

def test_insertion_retrieval_user():
    session = SessionLocal()
    
    new_user = User(
        Email="TestEmail@test.com",
        HashedPassword="test",
        IsActive=True
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    assert new_user.ID is not None
    assert new_user.Email == "TestEmail@test.com"
    assert new_user.HashedPassword == "test"
    assert new_user.IsActive == True
    
    session.delete(new_user)
    session.commit()
    session.close()
    
def test_insert_invalid_user():
    session = SessionLocal()
    
    incorrect_user = User(
        Email=None,
        HashedPassword="test",
        IsActive=True
    )
    
    session.add(incorrect_user)
    
    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
    session.close()

def test_insertion_retrieval_user_workout_request():
    session = SessionLocal()
    
    new_user = User(
        Email="TestEmail@test.com",
        HashedPassword="test",
        IsActive=True
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    new_workout = workouts(
        Name="Test Workout",
        Description="This is a test workout"
    )
    
    session.add(new_workout)
    session.commit()
    session.refresh(new_workout)
    
    new_user_workout_request = UserWorkoutRequest(
        UserID=new_user.ID,
        WorkoutID=new_workout.ID,
        RequestType="Test Gym Workout",
        Status="Test pending"
    )
    
    session.add(new_user_workout_request)
    session.commit()
    session.refresh(new_user_workout_request)
    
    assert new_user_workout_request.ID is not None
    assert new_user_workout_request.UserID == new_user.ID #tests valid foreign key insertion
    assert new_user_workout_request.WorkoutID == new_workout.ID #tests valid foreign key insertion
    assert new_user_workout_request.RequestType == "Test Gym Workout"
    assert new_user_workout_request.Status == "Test pending"
    
    session.delete(new_user_workout_request)
    session.delete(new_workout)
    session.delete(new_user)
    session.commit()
    session.close()
    
def test_insert_invalid_user_workout_request_type():
    session = SessionLocal()
    
    incorrect_user_workout_request = UserWorkoutRequest(
        RequestType=None,
        Status="Test pending"
    )
    
    session.add(incorrect_user_workout_request)
    
    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
    session.close()

def test_insert_invalid_foreign_key_user_workout_request():
    session = SessionLocal()
    
    bad_user_workout_request = UserWorkoutRequest(
        UserID=9999,
        RequestType="Test Gym Workout",
        Status="Test pending"
    )
    
    session.add(bad_user_workout_request)
    
    with pytest.raises(IntegrityError):
        session.commit()
        
    session.rollback()
    session.close()

def test_data_insertion_retrieval_user_profile():
    session = SessionLocal()
    
    new_user = User(
        Email="TestEmail@test.com",
        HashedPassword="test",
        IsActive=True
    )
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    new_user_profile = UserProfile(
        UserID=new_user.ID,
        FullName="Test",
        Age=23,
        HeightCM=176,
        WeightKG=78,
        FitnessLevel="Beginner",
        Goal="Lose Weight",
        InjuriesOrLimitations="N/A"
    )
    
    session.add(new_user_profile)
    session.commit()
    session.refresh(new_user_profile)
    
    assert new_user_profile.ID is not None
    assert new_user_profile.UserID == new_user.ID #tests valid foreign key insertion
    assert new_user_profile.FullName == "Test"
    assert new_user_profile.Age == 23
    assert new_user_profile.HeightCM == 176
    assert new_user_profile.WeightKG == 78
    assert new_user_profile.FitnessLevel == "Beginner"
    assert new_user_profile.Goal == "Lose Weight"
    assert new_user_profile.InjuriesOrLimitations == "N/A"
    
    session.delete(new_user_profile)
    session.delete(new_user)
    session.commit()
    session.close()
    
def test_insert_invalid_user_profile_name():
    session = SessionLocal()
    
    incorrect_user_profile = UserProfile(
        FullName=None,
        Age=23,
        HeightCM=176,
        WeightKG=78,
        FitnessLevel="Beginner",
        Goal="Lose Weight",
        InjuriesOrLimitations="N/A"
    )
    
    session.add(incorrect_user_profile)
    
    with pytest.raises(IntegrityError):
        session.commit()

    session.rollback()
    session.close()

def test_insert_invalid_foreign_key_user_profile():
    session = SessionLocal()
    
    bad_user_profile = UserProfile(
        UserID=9999,
        FullName="Test",
        Age=23,
        HeightCM=176,
        WeightKG=78,
        FitnessLevel="Beginner",
        Goal="Lose Weight",
        InjuriesOrLimitations="N/A"
    )
    
    session.add(bad_user_profile)
    
    with pytest.raises(IntegrityError):
        session.commit()
        
    session.rollback()
    session.close()