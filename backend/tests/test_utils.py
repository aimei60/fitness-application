#file for setting up sample data

import sys
print("PYTHONPATH:", sys.path)

from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts, workout_sections, workoutRoutine, User
from backend.application.utilities.security import get_password_hash
from backend.application.crud.profile import create_user_profile
from backend.application.models import UserProfile

#inserts workout, workout section and workout routine in the test db
def insert_sample_entire_workout(db):
    workout = workouts(Name="Test Workout", Description="Test Description")
    db.add(workout)
    db.commit()
    db.refresh(workout)
    
    section = workout_sections(SectionName = "Test Section",
                               SectionOrder=1,
                               WOID=workout.ID)
    db.add(section)
    db.commit()
    db.refresh(section)

    routine = workoutRoutine(
        Name="Test Routine",
        RepsDuration="10 reps",
        RoutineDescription="Just a test",
        ExerciseOrder=1,
        SectionID=section.ID)
    
    db.add(routine)
    db.commit()
    db.refresh(routine)
    
    return workout, section, routine
    
def insert_sample_user(db):
    test_user = User(Email="TestUser1@test.com", HashedPassword=get_password_hash("Orange23"), IsActive=True)
    
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    
    return test_user
