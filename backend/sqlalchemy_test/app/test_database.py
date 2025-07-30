"""
Sets up a database connection and session for the test_db database.
Used exclusively for running tests against a separate, isolated database.
Loads all ORM models required for testing.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.application.database import Base
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

from backend.application.models import (
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
