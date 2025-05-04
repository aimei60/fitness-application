import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy_test.app.test_database import Base, engine, SessionLocal
from database import workouts, workout_sections, workoutRoutine, User, UserWorkoutRequest, UserProfile

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
    
def test_insert_invalid_workout_sections():
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
    
