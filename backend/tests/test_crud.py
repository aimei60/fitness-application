import pytest
from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts
from backend.application.crud.workouts import get_all_workouts, get_workout_with_sections_and_routines
from backend.tests.test_utils import insert_sample_entire_workout

#insert workout sample data into the workouts table in the test db
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
    db.close()
        
        

        

    
    
    
    
