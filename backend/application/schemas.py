from pydantic import BaseModel, Field
from typing import List

#schema for workout routine table
class WorkoutRoutineRead(BaseModel): #user output - returns the below fields
    Name: str = Field(..., max_length=50)
    RepsDuration: str = Field(..., max_length=20)
    RoutineDescription: str = Field(..., max_length=225)
    ExerciseOrder: int
    
    class Config:
        orm_mode = True
        
#schema for workout section table
class WorkoutSectionRead(BaseModel): #user output returns section name
    SectionName: str = Field(..., max_length=50)
    Routines: List[WorkoutRoutineRead] = []
    
    class Config:
        orm_mode = True
    
#schema for workouts table
class WorkoutBase(BaseModel): #user input. User can type which workout they want
    Name: str = Field(..., max_length=50) #user input. Name in workouts has 50 max characters
    
class WorkoutRead(WorkoutBase): #user output returns the decscription of the workout
    Description: str
    Sections: List[WorkoutSectionRead] = []
    
    class Config:
        orm_mode = True