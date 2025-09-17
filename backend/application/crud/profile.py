#profile crud functions

from sqlalchemy.orm import Session
from backend.application.models import UserProfile
from backend.application.schemas import UserProfileCreate, UserProfileRead, UserProfileUpdate
from fastapi import HTTPException, status

#allows the user to create their profile on the application and enter details such as name, age, fitness level etc.
def create_user_profile(db: Session, user_id: int, profile: UserProfileCreate):
    existing_profile = db.query(UserProfile).filter(UserProfile.UserID == user_id).first()
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User profile already exists."
        )
    
    user_profile = UserProfile(
        UserID = user_id,
        FullName = profile.FullName,
        Age = profile.Age,
        HeightCM = profile.Height,
        WeightKG = profile.Weight,
        FitnessLevel = profile.FitnessLevel,
        Goal = profile.Goal,
        InjuriesOrLimitations = profile.InjuriesOrLimitations 
    )
    db.add(user_profile)
    db.commit()
    db.refresh(user_profile)
    return user_profile

#returns the profile for a specific user by user_id
def read_user_profile(db: Session, user_id: int):
    return db.query(UserProfile).filter(UserProfile.UserID == user_id).first()

#allows user to update their profile sections
def update_user_profile(db: Session, user_id: int, profile: UserProfileUpdate):
    user_profile = db.query(UserProfile).filter(UserProfile.UserID == user_id).first()
  
    if not user_profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User profile not found")
    
    if profile.FullName is not None:
        user_profile.FullName = profile.FullName
    if profile.Age is not None:
        user_profile.Age = profile.Age
    if profile.Height is not None:
        user_profile.HeightCM = profile.Height
    if profile.Weight is not None:
        user_profile.WeightKG = profile.Weight
    if profile.FitnessLevel is not None:
        user_profile.FitnessLevel = profile.FitnessLevel
    if profile.Goal is not None:
        user_profile.Goal = profile.Goal
    if profile.InjuriesOrLimitations is not None:
        user_profile.InjuriesOrLimitations = profile.InjuriesOrLimitations
        
    db.commit()
    db.refresh(user_profile)
    return user_profile