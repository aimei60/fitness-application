from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from application.database import get_db
from application.crud.user import create_user, get_user_email_and_active_status, update_user_password
from application.schemas import UserCreate, UserRead, UserPasswordChange

router = APIRouter()

#creates the user
@router.post("/users", response_model=UserRead)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)