"""
Sets up the database connection and ORM models for the fitness application.
Includes a database engine and session creation, core tables e.g. workouts, workout_sections etc. and environment variable loading for database credentials
"""

import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv("sens.env")

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
#Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

"""
Defines a workout template used to build exercise programs for users.
Each workout is broken into multiple sections for the workout_sections table.
"""
class workouts(Base):
    __tablename__ = "WorkOuts"
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str]
    
    T1 = relationship("workout_sections", back_populates="T2")

"""
Represents a section of a workout, such as Warm Up, Circuit, or Cool Down.
This table group defines the structure and order of a workout plan.
"""    
class workout_sections(Base):
    __tablename__ = "Workout_Sections" 
       
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    WOID: Mapped[int] = mapped_column(ForeignKey("WorkOuts.ID"))
    SectionName: Mapped[str] = mapped_column(String(50))
    SectionOrder: Mapped[int]
    
    T2 = relationship("workouts", back_populates="T1")
    
    T3 = relationship("workoutRoutine", back_populates="T4")

"""
Represents an individual exercise within a workout section.
Defines the exercise name, repetitions or duration, description, and execution order.
"""    
class workoutRoutine(Base):
    __tablename__ = "Workout_Routine"
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    SectionID: Mapped[int] = mapped_column(ForeignKey("Workout_Sections.ID"))
    Name: Mapped[str] = mapped_column(String(50))
    RepsDuration: Mapped[str] = mapped_column(String(20))
    RoutineDescription: Mapped[str] = mapped_column(String(255))
    ExerciseOrder: Mapped[int] = mapped_column(Integer)
    
    T4 = relationship("workout_sections", back_populates="T3")
    
"""
Represents an application user with login credentials and account status.
Linked to user profiles and workout table.
"""
class User(Base):
    __tablename__ = "users"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    Email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    HashedPassword: Mapped[str]
    IsActive: Mapped[bool] = mapped_column(default=True)
    
    workout_requests = relationship("UserWorkoutRequest", back_populates="users")
    
    profiles = relationship("UserProfile", uselist=False, back_populates="user")

"""
Represents a user's request for a specific workout program.
Tracks the request type and its current status (e.g., pending, approved, completed).
Linked to users table and workouts table.
"""      
class UserWorkoutRequest(Base):
    __tablename__ = "user_workout_requests"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    UserID: Mapped[int] = mapped_column(ForeignKey("users.ID"))
    WorkoutID: Mapped[int] = mapped_column(ForeignKey("WorkOuts.ID"))
    RequestType: Mapped[str] = mapped_column(String(100))
    Status: Mapped[str] = mapped_column(String(50), default="pending")
    
    users = relationship("User", back_populates="workout_requests")
    
    workout = relationship("workouts")

"""
Stores extended profile information for a user, including fitness level, goals, and physical metrics.
Each profile is linked one-to-one with a user account.
"""    
class UserProfile(Base):
    __tablename__ = "user_profiles"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    UserID: Mapped[int] = mapped_column(ForeignKey("users.ID"), unique=True)
    FullName: Mapped[str] = mapped_column(String(100))
    Age: Mapped[int] = mapped_column(nullable=True)
    HeightCM: Mapped[int] = mapped_column(nullable=True)
    WeightKG: Mapped[int] = mapped_column(nullable=True)
    FitnessLevel: Mapped[str] = mapped_column(String(100), nullable=True)
    Goal: Mapped[str] = mapped_column(String(200), nullable=True)
    InjuriesOrLimitations: Mapped[str] = mapped_column(String(255), nullable=True)
    
    user = relationship("User", back_populates="profiles")
