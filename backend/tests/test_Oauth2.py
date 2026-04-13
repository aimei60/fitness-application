#tests Oauth2 file
import pytest
import jwt
from fastapi import status, HTTPException
from sqlalchemy_test.app.testing_database import SessionLocal
from application import Oauth2
from application.models import User

@pytest.fixture(autouse=True)
def auth_constants(monkeypatch):
    monkeypatch.setattr(Oauth2, "JWT_SECRET", "test-secret", raising=False)
    monkeypatch.setattr(Oauth2, "JWT_ALGORITHM", "HS256", raising=False)
    monkeypatch.setattr(Oauth2, "JWT_EXPIRATION_MINUTES", 5, raising=False)

#test to create token, decode it verify the data matches correctly and has an expiry time     
def test_create_access_token():
    token = Oauth2.create_access_token({"user_id": 123, "role": "user"})
    payload = jwt.decode(token, Oauth2.JWT_SECRET, algorithms=[Oauth2.JWT_ALGORITHM])
    assert payload["user_id"] == 123
    assert payload["role"] == "user"
    assert "exp" in payload #confirms token has expiry time set

#verifies access token and confirms token data is correct
def test_verify_access_token():
    token = Oauth2.create_access_token({"user_id": 42})
    cred_exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized credentials")

    td = Oauth2.verify_access_token(token, cred_exc)
    assert td.id == "42"

#tests retrieivng the user correctly
def test_get_current_user_returns_user():
    db = SessionLocal()
    
    db.query(User).filter(User.Email == "TestUser@test.com").delete()
    db.commit()
    
    user = User(
        Email="TestUser@test.com",
        HashedPassword="test",
        IsActive=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    token = Oauth2.create_access_token({"user_id": user.ID})
    
    current = Oauth2.get_current_user(access_token=token, db=db)
    
    assert current.ID == user.ID
    assert current.Email == user.Email
    
    db.delete(user)
    db.commit()
    db.close()