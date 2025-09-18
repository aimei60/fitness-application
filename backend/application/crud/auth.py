#auth crud functions

from sqlalchemy.orm import Session
from application.models import User
from application.schemas import UserCreate
from application.utilities.security import get_password_hash

#retrieves user emails
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.Email == email).first()

#creates a user for the signup part
def create_user(db: Session, email: str, hashed_password: str):
    db_user = User(Email=email, HashedPassword=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
