from sqlalchemy.orm import Session
from backend.application.models import User
from schemas import UserCreate, UserRead, UserPasswordChange
from utilities.security import get_password_hash

#creates a new user and hashes the password and adds the user in the db
def create_user(db: Session, user: UserCreate):
    hash_pw = get_password_hash(user.Password)
    db_user = User(Email=user.Email, HashedPassword=hash_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#once I have implemented authentication, will update this function
def get_user_email_and_active_status(db: Session, user: UserRead):
    pass

#once I have implemented authentication, will update this function
def update_user_password(db: Session, user: UserPasswordChange):
    pass