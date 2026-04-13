#sets up a db connection and session for the test_db database. This is for running tests against a separate, isolated db.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from application.database import Base
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv("sens.env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/test_db")
SessionLocal = sessionmaker(bind=engine)

from application.models import (
    workouts,
    workout_sections,
    workoutRoutine,
    User,
    UserWorkoutRequest,
    UserProfile,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
