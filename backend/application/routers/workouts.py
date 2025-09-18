#workouts router functions

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from application.database import get_db
from application.models import User
from application.crud.workouts import get_all_workouts, get_workout_with_sections_and_routines
from application.schemas import WorkoutSimpleRead, WorkoutRead
from typing import List
from application import Oauth2

router = APIRouter(tags=['Workouts'])

#Returns the entire list of workouts for the user
@router.get("/workouts", response_model=List[WorkoutSimpleRead])
def read_workouts(db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    return get_all_workouts(db)

#Returns the user chosen workout in full for the user to utilise
@router.get("/workouts/{name}", response_model=WorkoutRead)
def read_chosen_workout(name: str, db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    workout = get_workout_with_sections_and_routines(db, name)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout
    
