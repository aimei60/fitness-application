from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from enum import Enum

#schema for workout routine table
class WorkoutRoutineRead(BaseModel): #output - returns the below fields
    Name: str = Field(..., max_length=50)
    RepsDuration: str = Field(..., max_length=20)
    RoutineDescription: str = Field(..., max_length=225)
    ExerciseOrder: int
    
    class Config:
        from_attributes = True
        
#schema for workout section table
class WorkoutSectionRead(BaseModel): #output returns section name
    SectionName: str = Field(..., max_length=50)
    Routines: List[WorkoutRoutineRead] = []
    
    class Config:
        from_attributes = True
    
#schema for workouts table
class WorkoutBase(BaseModel): #user input. User can type which workout they want
    Name: str = Field(..., max_length=50) #user input. Name in workouts has 50 max characters
    
class WorkoutRead(WorkoutBase): #output returns the decscription of the workout
    Sections: List[WorkoutSectionRead] = []
    
    class Config:
        from_attributes = True
        
class WorkoutSimpleRead(WorkoutBase): #output returns workout name and workout description
    Description: str
    
    class Config:
        from_attributes = True
        
#schema for user table
class UserCreate(BaseModel): #user input to create profile 
    Email: EmailStr
    Password: str = Field(..., min_length=8)
    
class UserRead(BaseModel):#having this incase I want these details to be shown in the settings page 
    Email: EmailStr
    IsActive: bool
    
    class Config:
        ofrom_attributes = True
        
class UserPasswordChange(BaseModel): #user input to change password
    current_password: str
    new_password: str = Field(..., min_length=8)
    
#schema for user request - the below schema is optional for the user and if the user wants to request a more tailored or reviewed workout plan
class RequestTypeEnum(str, Enum):
    new_workout = "new_workout" #User wants a new plan 
    repeat_workout = "repeat_workout" #User wants to re-do their last plan
    upgrade_level = "upgrade_level" #User thinks they’ve progressed to next level e.g. beginner to intermediate
    rehab_plan = "rehab_plan" #Recovery/injury-related requests
    
class UserWorkoutRequestCreate(BaseModel): #user input
    RequestType: RequestTypeEnum

class UserWorkoutRequestRead(BaseModel): #user output
    RequestType: RequestTypeEnum
    Status: str

    class Config:
        from_attributes = True

#schema for user to update status
class RequestStatusEnum(str, Enum):
    pending = "pending" #request is pending
    active = "active" #request is active 
    completed = "completed" #request is completed
 
class UpdateRequestStatus(BaseModel): #user input
    Status: RequestStatusEnum 

#schema for user profile
class UserProfileCreate(BaseModel): #user input
    FullName: str = Field(..., max_length=100)
    Age: Optional[int]
    Height: Optional[int]
    Weight: Optional[int]
    FitnessLevel: Optional[str] = Field(..., max_length=100)
    Goal: str = Field(..., max_length=100)
    InjuriesOrLimitations: Optional[str] = Field(None, max_length=255)
    
class UserProfileRead(BaseModel): #output
    ID: int
    FullName: str = Field(..., max_length=100)
    Age: Optional[int]
    Height: Optional[int]
    Weight: Optional[int]
    FitnessLevel: Optional[str] = Field(None, max_length=100)
    Goal: str= Field(..., max_length=200)
    InjuriesOrLimitations: Optional[str] = Field(None, max_length=255)

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
     Email: EmailStr
     Password: str
     
class Token(BaseModel): #output sent to user after login
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None