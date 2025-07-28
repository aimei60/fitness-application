from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from application.database import get_db
from application.crud import auth
from application import Oauth2
from application.schemas import UserProfileCreate, UserProfileUpdate, UserProfileRead
from application.crud.profile import create_user_profile, read_user_profile, update_user_profile
from application.models import User

router = APIRouter(tags=['Profile'])

#allows user to create their profile section
@router.post("/profile", response_model=UserProfileRead)
def create_profile(profile: UserProfileCreate, db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    return create_user_profile(db, current_user.ID, profile)

#returns the user's profile
@router.get("/profile/summary", response_model=UserProfileRead)
def return_user_profile(db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    return read_user_profile(db, current_user.ID)

#allows user to update the their profile details
@router.post("/profile/update-profile", response_model=UserProfileRead)
def update_profile(input: UserProfileUpdate, db: Session = Depends(get_db), current_user: User = Depends(Oauth2.get_current_user)):
    return update_user_profile(db, current_user.ID, input)