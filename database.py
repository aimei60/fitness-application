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

class workouts(Base):
    __tablename__ = "WorkOuts"
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    Name: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str]
    
    T1 = relationship("workout_sections", back_populates="T2")
    
class workout_sections(Base):
    __tablename__ = "Workout_Sections" 
       
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    WOID: Mapped[int] = mapped_column(ForeignKey("WorkOuts.ID"))
    SectionName: Mapped[str] = mapped_column(String(50))
    SectionOrder: Mapped[int]
    
    T2 = relationship("workouts", back_populates="T1")
    
    T3 = relationship("workoutRoutine", back_populates="T4")
    
class workoutRoutine(Base):
    __tablename__ = "Workout_Routine"
    
    ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    SectionID: Mapped[int] = mapped_column(ForeignKey("Workout_Sections.ID"))
    Name: Mapped[str] = mapped_column(String(50))
    RepsDuration: Mapped[str] = mapped_column(String(20))
    RoutineDescription: Mapped[str] = mapped_column(String(255))
    ExerciseOrder: Mapped[int] = mapped_column(Integer)
    
    T4 = relationship("workout_sections", back_populates="T3")

class User(Base):
    __tablename__ = "users"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    Email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    HashedPassword: Mapped[str]
    IsActive: Mapped[bool] = mapped_column(default=True)
    
    workout_requests = relationship("UserWorkoutRequest", back_populates="users")
    
class UserWorkoutRequest(Base):
    __tablename__ = "user_workout_requests"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    UserID: Mapped[int] = mapped_column(ForeignKey("users.ID"))
    WorkoutID: Mapped[int] = mapped_column(ForeignKey("WorkOuts.ID"))
    RequestType: Mapped[str] = mapped_column(String(100))
    Status: Mapped[str] = mapped_column(String(50), default="pending")
    
    users = relationship("User", back_populates="workout_requests")
    workout = relationship("workouts")
    
