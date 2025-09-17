#user crud functions

from sqlalchemy.orm import Session
from backend.application.models import User
from backend.application.schemas import UserCreate, UserRead, UserPasswordChange
from backend.application.utilities.security import get_password_hash
from passlib.context import CryptContext
from fastapi import status, HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#creates a new user and hashes the password and adds the user in the db
def create_user(db: Session, user: UserCreate):
    hash_pw = get_password_hash(user.Password)
    db_user = User(Email=user.Email, HashedPassword=hash_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#returns the user's email address and active status
def get_user_email_and_active_status(user: User):
    return UserRead(Email=user.Email, IsActive=user.IsActive)

#verifies current password, hashes new password and update user record and confirms the password change
def update_user_password(db: Session, user_input: UserPasswordChange, current_user: User):
    if not pwd_context.verify(user_input.current_password, current_user.HashedPassword):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="status_code=status.HTTP_403_FORBIDDEN")
    
    hashed_new_pw = pwd_context.hash(user_input.new_password)
    
    current_user.HashedPassword = hashed_new_pw
    db.commit()
    
    return {"message": "Password updated successfully"}