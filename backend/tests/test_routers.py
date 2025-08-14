from fastapi.testclient import TestClient
from backend.main import app
from backend.application.database import get_db
from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts, User
from backend.application import Oauth2

#test override db
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = override_get_db #overrides get_db

client = TestClient(app)

#function to create token and authenticate user for the below tests    
def auth_header(db):
    user = db.query(User).filter(User.Email == "test@example.com").one()
    token = Oauth2.create_access_token({"user_id": user.ID})
    return {"Authorization": f"Bearer {token}"}

#tests the retrieval of all of the workouts by adding fake workouts, having a test user sign in - creating a token and confirming the test data is added in there.
def test_read_all_workouts():
    db = SessionLocal()
    
    w1 = workouts(Name="HIIT Workout", Description="Test HIIT")
    w2 = workouts(Name="Athlete Workout", Description="Test Athlete")
    db.add(w1)
    db.add(w2)
    db.commit()
    db.refresh(w1)
    db.refresh(w2)
    
    auth = client.get("/workouts", headers=auth_header(db))
    
    assert auth.status_code == 200
    data = auth.json()
    
    names = set()
    for w in data:
        names.add(w["Name"])
        
    assert "HIIT Workout" in names 
    assert "Athlete Workout" in names
    
    db.delete(w1)
    db.delete(w2)
    db.commit()
    db.close()

#test to the correct workout is retrieved based on authenticated user request    
def test_specific_workout():
    db = SessionLocal()

    w = workouts(Name="HIIT Workout", Description="Test HIIT")
    db.add(w)
    db.commit()
    db.refresh(w)
    
    response = client.get(f"/workouts/{w.Name}", headers=auth_header(db))
  
    assert response.status_code == 200
    data = response.json()
    assert data["Name"] == "HIIT Workout"
    
    db.delete(w)
    db.commit()
    db.close()

#tests the correct error is raised when a workout not on the list is requested
def test_error_workout_retrieval():
    db = SessionLocal()

    resp = client.get("/workouts/error-workout", headers=auth_header(db))

    assert resp.status_code == 404
    data = resp.json()
    assert data["detail"] == "Workout not found"

    db.close()
  
    