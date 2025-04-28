from sqlalchemy_test.app.test_database import Base, engine, SessionLocal
from database import workouts, workout_sections, workoutRoutine, User, UserWorkoutRequest, UserProfile

Base.metadata.create_all(engine)

def test_dummy():
    assert True
    