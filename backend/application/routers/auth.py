#auth router functions

from fastapi import APIRouter, Depends, status, HTTPException, Response, Request
import secrets
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from application.database import get_db
from application.utilities import security
from application.schemas import UserLogin, UserSignup
from application.crud.auth import get_user_by_email, create_user
from application import Oauth2, models
from application.rate_limit import limiter
import os

router = APIRouter(tags=['Authentication'])

ENV = os.getenv("ENV", "development").lower()
IS_PROD = ENV in {"prod", "production"}

#Central cookie
COOKIE_DOMAIN = os.getenv("COOKIE_DOMAIN", ".fitrequest.dev" if IS_PROD else "")
COOKIE_KW = dict(
    httponly=True,
    secure=IS_PROD,      
    samesite=("none" if IS_PROD else "lax"), 
    path="/",
    **({"domain": COOKIE_DOMAIN} if COOKIE_DOMAIN else {})
)

#stores jwt securely in a cookie that js cannot access and creates and stores a CSRF token in a separate cookie that js can read
def set_auth_cookies(response: Response, access_jwt: str):
    # httpOnly auth cookie (browser sends it automatically to the API origin)
    response.set_cookie("access_token", access_jwt, **COOKIE_KW)

    # CSRF token for your frontend to read and echo back in a header
    csrf = secrets.token_urlsafe(32)
    response.set_cookie(
        "csrf_token",
        csrf,
        httponly=False,       
        secure=IS_PROD,
        samesite=("none" if IS_PROD else "lax"),       
        path="/",
        **({"domain": COOKIE_DOMAIN} if COOKIE_DOMAIN else {})
    )
    return csrf

#user sign up: checks if email already exists, if not creates a new user and issues a new token
@router.post("/signup")
def signup(user: UserSignup, db: Session = Depends(get_db), response: Response = None):
    if get_user_by_email(db, user.Email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = security.get_password_hash(user.Password)

    new_user = create_user(db, email=user.Email, hashed_password=hashed_pw)

    access_token = Oauth2.create_access_token({"user_id": new_user.ID})
    set_auth_cookies(response, access_token)
    return {"ok": True}


#for Swagger UI
#authenticates the user and verifies their password and if correct, generates and returns a JWT access token
@router.post('/login/form')
def dev_login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), response: Response = None):
    user = get_user_by_email(db, user_credentials.username)
    
    if not user or not security.verify_password(user_credentials.password, user.HashedPassword):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")    
    access_token = Oauth2.create_access_token(data={"user_id": user.ID})
    set_auth_cookies(response, access_token)
    return {"ok": True}

#Json based login route for users
@router.post('/login')
@limiter.limit("5/minute")  #5 login attempts per minute per IP
def user_login(user_credentials: UserLogin, request: Request, db: Session = Depends(get_db), response: Response = None):
    user = get_user_by_email(db, user_credentials.Email)
    
    if not user or not security.verify_password(user_credentials.Password, user.HashedPassword):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Username or Password")

    access_token = Oauth2.create_access_token(data={"user_id": user.ID})
    set_auth_cookies(response, access_token)
    return {"ok": True}

#helper function to check login flow 
@router.get("/me")
def read_me(current_user: models.User = Depends(Oauth2.get_current_user)):
    return {"id": current_user.ID, "email": current_user.Email}

