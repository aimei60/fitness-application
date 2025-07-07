from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.database import get_db
from application.crud.workouts import get_all_workouts, get_workout_with_sections_and_routines
from application.schemas import WorkoutSimpleRead, WorkoutRead
from typing import List

router = APIRouter()

@router.get("/workouts", response_model=List[WorkoutSimpleRead])
def read_workouts(db: Session = Depends(get_db)):
    return get_all_workouts(db)

@router.get("/workouts/{name}", response_model=WorkoutRead)
def read_chosen_workout(name: str, db: Session = Depends(get_db)):
    workout = get_workout_with_sections_and_routines(db, name)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout
    
