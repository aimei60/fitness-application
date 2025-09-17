#user router functions

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.application.database import get_db
from backend.application.crud.user import create_user, get_user_email_and_active_status, update_user_password
from backend.application.schemas import UserCreate, UserRead, UserPasswordChange
from backend.application import Oauth2
from backend.application.models import User

router = APIRouter(tags=['User'])

#creates the user
@router.post("/users", response_model=UserRead)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

#returns the user's email address and active status
@router.get("/me", response_model=UserRead)
def get_user_summary(current_user: User = Depends(Oauth2.get_current_user)):
    return get_user_email_and_active_status(current_user)

#router function to update the user's password
@router.post("/user/change-password")
def change_password(input: UserPasswordChange, db: Session = Depends(get_db), current_user = Depends(Oauth2.get_current_user)):
    return update_user_password(db, input, current_user)
