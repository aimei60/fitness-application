from sqlalchemy.orm import Session, joinedload
from backend.application.models import workouts, workout_sections

#shows the user all available workout options
def get_all_workouts(db: Session):
    return db.query(workouts).all()

#returns the workout name, description, section and the workout routine for the user
def get_workout_with_sections_and_routines(db: Session, name: str):
    return (db.query(workouts).options(joinedload(workouts.T1).joinedload(workout_sections.T3)).filter(workouts.Name.ilike(name)).first())