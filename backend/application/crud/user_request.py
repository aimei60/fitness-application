from sqlalchemy.orm import Session
from typing import Optional
from backend.application.models import UserWorkoutRequest
from schemas import UserWorkoutRequestCreate, RequestStatusEnum

#user creates workout request
def create_workout_request(db: Session, user_id: int, request: UserWorkoutRequestCreate):
    db_request = UserWorkoutRequest(
        UserID = user_id,
        WorkoutID = request.WorkoutID,
        RequestType = request.RequestType.value,
        Status = "Pending"
        )
    
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

#returns the users workout requests, later on I will filter this so user can choose to filter by active or pending
def read_workout_request(db: Session, user_id: int, status: Optional[str] = None):
    query = db.query(UserWorkoutRequest).filter(UserWorkoutRequest.UserID == user_id)
    if status:
        query = query.filter(UserWorkoutRequest.Status == status)
    return query.all()

#allows the user to update the request status
def update_request_status(db: Session, request_id: int, new_status: RequestStatusEnum):
    request = db.query(UserWorkoutRequest).filter(UserWorkoutRequest.ID == request_id).first()
    if request:
        request.Status = new_status.value
        db.commit()
        db.refresh(request)
    return request
    

