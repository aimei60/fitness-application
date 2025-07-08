from sqlalchemy.orm import Session
from application.models import User

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.Email == email).first()