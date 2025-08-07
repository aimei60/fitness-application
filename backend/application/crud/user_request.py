from sqlalchemy.orm import Session
from typing import Optional
from fastapi import HTTPException, status
from backend.application.models import workouts, UserWorkoutRequest, workouts
from backend.application.schemas import UserWorkoutRequestCreate, RequestStatusEnum, RequestTypeEnum
from backend.application.crud.workouts import get_workout_with_sections_and_routines

#allows the user to create a workout request and updates the request with a selected workout
def create_workout_request(db: Session, user_id: int, request: UserWorkoutRequestCreate):
    db_request = UserWorkoutRequest(
        UserID = user_id,
        RequestType = request.request_type.value,
        Status = "Pending"
        )
    
    db.add(db_request)

    workout = None
    with db.no_autoflush:
        if request.request_type == RequestTypeEnum.new_workout:
            workout = db.query(workouts).filter(workouts.Name == "Everyday movement Workout").first()

        elif request.request_type == RequestTypeEnum.repeat_workout:
            last_request = (
                db.query(UserWorkoutRequest)
                .filter(UserWorkoutRequest.UserID == user_id, UserWorkoutRequest.WorkoutID.isnot(None))
                .order_by(UserWorkoutRequest.ID.desc())
                .first()
                )
            if last_request:
                workout = db.query(workouts).filter(workouts.ID == last_request.WorkoutID).first()

        elif request.request_type == RequestTypeEnum.upgrade_level:
            workout = db.query(workouts).filter(workouts.Name == "Endurance Workout").first()

        elif request.request_type == RequestTypeEnum.rehab_plan:
            workout = db.query(workouts).filter(workouts.Name == "Recovery rehabilitation Workout").first()

    if workout:
        db_request.WorkoutID = workout.ID
        db.commit()
        db.refresh(db_request)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Workout not found for request type")
    
    full_workout = get_workout_with_sections_and_routines(db, workout.Name)
    return full_workout

"""#returns the users workout requests, later on I will filter this so user can choose to filter by active or pending
def read_workout_request(db: Session, user_id: int, status: Optional[str] = None):
    query = db.query(UserWorkoutRequest).filter(UserWorkoutRequest.UserID == user_id)
    if status:
        query = query.filter(UserWorkoutRequest.Status == status)
    return query.all()

"""
