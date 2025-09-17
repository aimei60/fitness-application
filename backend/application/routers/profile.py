#profile router functions

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.application.database import get_db
from backend.application.crud import auth
from backend.application import Oauth2
from backend.application.schemas import UserProfileCreate, UserProfileUpdate, UserProfileRead
from backend.application.crud.profile import create_user_profile, read_user_profile, update_user_profile
from backend.application.models import User

router = APIRouter(tags=['Profile'])

#allows user to create their profile section
@router.post("/profile", response_model=UserProfileRead)
def create_profile(profile: UserProfileCreate, db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    return create_user_profile(db, current_user.ID, profile)

#returns the user's profile
@router.get("/profile", response_model=UserProfileRead)
def return_user_profile(db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    profile = read_user_profile(db, current_user.ID)
    
    if profile is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile

#allows user to update the their profile details
@router.patch("/profile", response_model=UserProfileRead)
def update_profile(input: UserProfileUpdate, db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    updated = update_user_profile(db, current_user.ID, input)
    
    if updated is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return updated