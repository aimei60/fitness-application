import os
from dotenv import load_dotenv
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class workouts(Base):
    __tablename__ = "WorkOuts"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str]
    
    T1 = relationship("workout_sections", back_populates="T2")
    
class workout_sections(Base):
    __tablename__ = "Workout_Sections" 
       
    ID: Mapped[int] = mapped_column(primary_key=True)
    WOID: Mapped[int] = mapped_column(ForeignKey("WorkOuts.ID"))
    SectionName: Mapped[str] = mapped_column(String(10))
    SectionOrder: Mapped[int]
    
    T2 = relationship("workouts", back_populates="T1")
    
    T3 = relationship("workoutRoutine", back_populates="T4")
    
class workoutRoutine(Base):
    __tablename__ = "Workout_Routine"
    
    ID: Mapped[int] = mapped_column(primary_key=True)
    SectionID = Mapped[int] = mapped_column(ForeignKey("Workout_Sections.ID"))
    Name: Mapped[str] = mapped_column(String(50))
    RepsDuration: Mapped[str] = mapped_column(String(20))
    RoutineDescription = Mapped[str]
    ExerciseOrder = Mapped[int]
    
    T4 = relationship("workout_sections", back_populates="T3")
    
load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
