from sqlalchemy.orm import Session, joinedload
from models import workouts

#shows the user all available workout options
def get_all_workouts(db: Session):
    return db.query(workouts).all()

#returns the workout name, description, section and the workout routine for the user
def get_workout_with_sections_and_routines(db: Session, name: str):
    return (db.query(workouts).options(joinedload(workouts.T1).joinedload("T3")).filter(workouts.Name == name).first())