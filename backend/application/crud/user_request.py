from sqlalchemy.orm import Session
from models import UserWorkoutRequest
from schemas import UserWorkoutRequestCreate, UserWorkoutRequestRead

def create_workout_request(db: Session, request: UserWorkoutRequestCreate):
    pass

def read_workout_request(db: Session, request: UserWorkoutRequestRead):
    pass