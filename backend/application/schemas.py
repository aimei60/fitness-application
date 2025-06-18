from pydantic import BaseModel, Field, EmailStr
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
        
#schema for user table
class UserCreate(BaseModel): #user input to create profile 
    Email: EmailStr
    Password: str = Field(..., min_length=8)
    
class UserRead(BaseModel):#having this incase I want these details to be shown in the settings page 
    Email: EmailStr
    IsActive: bool
    
    class Config:
        orm_mode = True
        
class UserPasswordChange(BaseModel): #user input to change password
    current_password: str
    new_password: str = Field(..., min_length=8)