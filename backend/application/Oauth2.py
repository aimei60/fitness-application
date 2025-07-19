from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from application import schemas, database, models
from sqlalchemy.orm import Session


load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES", 60))

if JWT_SECRET_KEY is None:
        raise ValueError("JWT_SECRET_KEY environment variable is required")
    
#Create access token for when the user logs in
def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    
    return encoded_jwt

#Decodes the token, validates the token is correct, checks if the user_id is present, and returns the user_id in TokenData format
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=str(user_id))
    except InvalidTokenError:
        raise credentials_exception
    
    return token_data

#Extracts token from the request, verifies the token, queries the db for the user with user ID from the token and raises an error if anything goes wrong
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token_data = verify_access_token(token, credentials_exception)
    
    user = db.query(models.User).filter(models.User.ID == int(token_data.id)).first()
    if not user:
        raise credentials_exception
    
    return user
    
    