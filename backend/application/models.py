"""
Defines the ORM models (tables) for the fitness application.
Includes core tables e.g. workouts, workout_sections etc.
"""

from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base
from typing import Optional

"""
Defines a workout template used to build exercise programs for users.
Each workout is broken into multiple sections for the workout_sections table.
"""
class workouts(Base):
    __tablename__ = "WorkOuts"
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str]
    
    Sections = relationship("workout_sections", back_populates="Workout")

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
    
    Routines = relationship("workoutRoutine", back_populates="Section")
    
    Workout = relationship("workouts", back_populates="Sections")

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
    
    Section = relationship("workout_sections", back_populates="Routines")
    
"""
Represents an application user with login credentials and account status.
Linked to user profiles and workout table.
"""
class User(Base):
    __tablename__ = "users"
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
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
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    UserID: Mapped[int] = mapped_column(ForeignKey("users.ID"))
    WorkoutID: Mapped[Optional[int]] = mapped_column(ForeignKey("WorkOuts.ID"), nullable=True)
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
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    UserID: Mapped[int] = mapped_column(ForeignKey("users.ID"), unique=True)
    FullName: Mapped[str] = mapped_column(String(100))
    Age: Mapped[int] = mapped_column(nullable=True)
    HeightCM: Mapped[int] = mapped_column(nullable=True)
    WeightKG: Mapped[int] = mapped_column(nullable=True)
    FitnessLevel: Mapped[str] = mapped_column(String(100), nullable=True)
    Goal: Mapped[str] = mapped_column(String(200), nullable=True)
    InjuriesOrLimitations: Mapped[str] = mapped_column(String(255), nullable=True)
    
    user = relationship("User", back_populates="profiles")