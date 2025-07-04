from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.application.database import get_db
from backend.application.crud.workouts import get_all_workouts
from backend.application.schemas import WorkoutRead
from typing import List

router = APIRouter()

@router.get("/workouts", response_model=List[WorkoutRead])
def read_workouts(db: Session = Depends(get_db)):
    return get_all_workouts(db)
