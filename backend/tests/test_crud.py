import pytest
from backend.sqlalchemy_test.app.test_database import Base, engine, SessionLocal
from backend.application.models import workouts, workout_sections, workoutRoutine
from backend.application.crud.workouts import get_all_workouts

"""def insert_test_workout(db):
    workout = workouts(Name="Test 1", Description="Test Description 1")
    db.add(workout)
    db.commit()
    db.refresh(workout)
    return workout

def test_workout_retrieval():
    db = SessionLocal()
    try:
        inserted = insert_test_workout(db)
        
        results = get_all_workouts(db)

        names = []
        for w in results:
            names.append(w.Name)
        assert inserted.Name in names
    finally:
        db.close()"""
        
    
    
    
    
    
