from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from application.database import get_db
from application.utilities import security
from application.crud import auth
from application import Oauth2

router = APIRouter(tags=['Authentication'])

#authenticates the user and verifies their password and if correct, generates and returns a JWT access token
@router.post('/login')
def user_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.get_user_by_email(db, user_credentials.username)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")
    
    if not security.verify_password(user_credentials.password, user.HashedPassword):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")
    
    access_token = Oauth2.create_access_token(data={"user_id": user.ID})
    
    return {"access_token": access_token, "token_type": "bearer"}