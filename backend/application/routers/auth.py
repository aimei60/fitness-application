from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from backend.application.database import get_db
from backend.application.utilities import security
from backend.application.schemas import UserLogin, UserSignup, Token
from backend.application.crud.auth import get_user_by_email, create_user
from backend.application import Oauth2, database, models

router = APIRouter(tags=['Authentication'])

#user sign up: checks if email already exists, if not creates a new user and issues a new token
@router.post("/signup", response_model=Token)
def signup(user: UserSignup, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.Email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = security.get_password_hash(user.Password)

    new_user = create_user(db, email=user.Email, hashed_password=hashed_pw)

    access_token = Oauth2.create_access_token({"user_id": new_user.ID})
    return {"access_token": access_token, "token_type": "bearer"}


#for Swagger UI
#authenticates the user and verifies their password and if correct, generates and returns a JWT access token
@router.post('/login/form')
def dev_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_credentials.username)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")
    
    if not security.verify_password(user_credentials.password, user.HashedPassword):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")
    
    access_token = Oauth2.create_access_token(data={"user_id": user.ID})
    
    return {"access_token": access_token, "token_type": "bearer"}

#Json based login route for users
@router.post('/login', response_model=Token)
def user_login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_email(db, user_credentials.Email)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")
    
    if not security.verify_password(user_credentials.Password, user.HashedPassword):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")
    
    access_token = Oauth2.create_access_token(data ={"user_id": user.ID})
    
    return {"access_token": access_token, "token_type": "bearer"}

#helper function to check login flow 
@router.get("/me")
def read_me(current_user: models.User = Depends(Oauth2.get_current_user)):
    return {"id": current_user.ID, "email": current_user.Email}