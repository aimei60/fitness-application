#authentication / JWT file

from fastapi import Depends, HTTPException, status, Cookie
import jwt
from jwt.exceptions import InvalidTokenError
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from application import schemas, database, models
from sqlalchemy.orm import Session
from typing import Optional

#let production use Fly secrets; only local dev loads .env/sens.env
if not os.getenv("FLY_APP_NAME") and not os.getenv("DISABLE_DOTENV"):
    load_dotenv(override=False)

JWT_SECRET = (
    os.getenv("JWT_SECRET")
    or os.getenv("JWT_SECRET_KEY")
    or os.getenv("SECRET_KEY")
)
if not JWT_SECRET:
    raise ValueError("Set JWT secret in env (JWT_SECRET or JWT_SECRET_KEY).")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
#getenv returns a string; default as string to avoid type issues
JWT_EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES", "60"))

#creates access token for when the user logs in
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt

#decodes the token, validates it, checks user_id, returns TokenData
def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id: str | None = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=str(user_id))
    except InvalidTokenError:
        raise credentials_exception
    return token_data

#looks for the access token cookie, verifies the jwt in cookie, finds user in db and returns authenticated user
def get_current_user(
    access_token: Optional[str] = Cookie(default=None),
    db: Session = Depends(database.get_db),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if not access_token:
        raise credentials_exception

    token_data = verify_access_token(access_token, credentials_exception)
    user = db.query(models.User).filter(models.User.ID == int(token_data.id)).first()
    if not user:
        raise credentials_exception
    return user