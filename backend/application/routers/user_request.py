from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from application.database import get_db
from application.crud.user_request import create_workout_request, read_workout_request, update_request_status
from application.schemas import UserWorkoutRequestCreate, UserWorkoutRequestRead, UpdateRequestStatus

router = APIRouter()

@router.post("/users/{user_id}/requests", response_model=UserWorkoutRequestRead)
def create_request(user_id: int, request: UserWorkoutRequestCreate, db: Session = Depends(get_db)):
    return create_workout_request(db, user_id, request)