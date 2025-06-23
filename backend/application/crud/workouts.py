from sqlalchemy.orm import Session
from models import workouts

#shows the user all available workout options
def get_all_workouts(db: Session):
    return db.query(workouts).all()

#searches for one specific workout by the workout name - user selects workout
def get_workout_name(db: Session, name: str):
    return db.query(workouts).filter(workouts.Name == name).first()

