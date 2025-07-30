import sys
print("PYTHONPATH:", sys.path)

from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts, workout_sections, workoutRoutine

def insert_sample_entire_workout(db):
    #insert workout 
    workout = workouts(Name="Test Workout", Description="Test Description")
    db.add(workout)
    db.commit()
    db.refresh(workout)
    
    #insert workout section
    section = workout_sections(SectionName = "Test Section",
                               SectionOrder=1,
                               WOID=workout.ID)
    db.add(section)
    db.commit()
    db.refresh(section)
    
    #insert workout routine
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
    
    
if __name__ == "__main__":
    db = SessionLocal()
    try:
        #insert_sample_entire_workout(db)
        print("✅ Inserted test data from test_utils.py")
    finally:
        db.close()





