from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from application.database import get_db
from application.schemas import UserLogin
from application.utilities import security
from application.crud import auth

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def user_login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = auth.get_user_by_email(db, user_credentials.Email)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Username or Password")
    
    if not security.verify_password(user_credentials.Password, user.HashedPassword):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Username or Password")
    
    return {"token: example token"}