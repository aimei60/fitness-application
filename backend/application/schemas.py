from pydantic import BaseModel, Field

class WorkoutBase(BaseModel):
    Name: str = Field(..., max_length=50) #Name in workouts has 50 max characters
    Description: str
    
class WorkoutRead(WorkoutBase):
    ID: int
    
    class config:
        orm_mode = True
        
