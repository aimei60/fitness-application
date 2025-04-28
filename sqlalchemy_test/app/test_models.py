import pytest
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
    