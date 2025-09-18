#user request router functions

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from application.database import get_db
from application.crud.user_request import create_workout_request
from application.schemas import UserWorkoutRequestCreate, UserWorkoutRequestRead, WorkoutRead, UpdateRequestStatus
from application import Oauth2
from application.models import User

router = APIRouter(tags=['User Request'])

#allows the user to make a specific request
@router.post("/users/requests", response_model=WorkoutRead)
def create_request(request: UserWorkoutRequestCreate, db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    return create_workout_request(db, current_user.ID, request)