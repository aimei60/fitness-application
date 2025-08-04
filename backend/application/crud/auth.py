from sqlalchemy.orm import Session
from backend.application.models import User

#retrieves user emails
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.Email == email).first()