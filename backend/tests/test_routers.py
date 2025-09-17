#tests the router functions

from fastapi.testclient import TestClient
from backend.main import app
from backend.application.database import get_db
from backend.sqlalchemy_test.app.test_database import SessionLocal
from backend.application.models import workouts, User, UserWorkoutRequest, UserProfile
from backend.application import Oauth2
from backend.application.crud.user import pwd_context

#test override db
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = override_get_db #overrides get_db

client = TestClient(app)

#ensures my tests always has a user otherwise some of my tests fail when inserting a user from the test table directly in the test function
def ensure_test_user(db, email="test@example.com", password="test"):
    user = db.query(User).filter(User.Email == email).one_or_none()
    if user is None:
        user = User(
            Email=email,
            HashedPassword=pwd_context.hash(password),
            IsActive=True,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

#function to create token and authenticate user for the below tests    
def auth_header(db):
    user = ensure_test_user(db)
    token = Oauth2.create_access_token({"user_id": user.ID})
    return {"Authorization": f"Bearer {token}"}

#WORKOUTS.PY ROUTER FUNCTION TESTS

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

    response = client.get("/workouts/error-workout", headers=auth_header(db))

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Workout not found"

    db.close()
  
#USER.PY ROUTER FUNCTION TESTS

#tests successful creation of new user
def test_create_user():
    db = SessionLocal()
    
    user = {
        "Email": "newuser2@example.com",
        "Password": "password098",
        "IsActive": "True"
    }

    response = client.post("/users", json=user)
    
    assert response.status_code == 200 
    data = response.json()
    assert data["Email"] == "newuser2@example.com"

    row = db.query(User).filter(User.Email == "newuser2@example.com").first()
    assert row is not None
    
    db.delete(row)
    db.commit()
    db.close()

#tests the user's email and active status is returned correctly
def test_get_user_details():
    db = SessionLocal()

    response = client.get("/me", headers=auth_header(db))
    assert response.status_code == 200
    data = response.json()
    assert data["Email"] == "test@example.com"
    assert data["IsActive"] == True

    db.close()

#tests a successful change of password for the user
def test_change_password_success():
    db = SessionLocal()

    user = ensure_test_user(db)
    user.HashedPassword = pwd_context.hash("test")
    db.commit()
    db.refresh(user)

    passwords = {"current_password": "test", "new_password": "test1234!"}
    response = client.post("/user/change-password", json=passwords, headers=auth_header(db))

    assert response.status_code == 200
    assert response.json()["message"] == "Password updated successfully"

    db.refresh(user)
    assert pwd_context.verify("test1234!", user.HashedPassword)

    db.close()

#tests the correct 403 error is raised when the wrong password is entered when trying to update user's password    
def test_change_password_wrong_current_password():
    db = SessionLocal()

    user = ensure_test_user(db)
    user.HashedPassword = pwd_context.hash("test")
    db.commit()
    db.refresh(user)

    passwords = {"current_password": "wrongpassword", "new_password": "test1234!"}

    response = client.post("/user/change-password", json=passwords, headers=auth_header(db))

    assert response.status_code == 403
    assert response.json()["detail"] == "status_code=status.HTTP_403_FORBIDDEN"

    db.close()

#USER_REQUEST.PY ROUTER FUNCTION TESTS

#tests the correct response is raised when "new workout" is requested
def test_create_request_new_workout_success():
    db = SessionLocal()
    
    w = workouts(Name="Everyday movement Workout", Description="workout")
    db.add(w); db.commit(); db.refresh(w)

    response = client.post("/users/requests", json={"request_type": "new_workout"}, headers=auth_header(db))
    
    assert response.status_code == 200
    data = response.json()
    assert data["Name"] == "Everyday movement Workout"
    
    db.query(UserWorkoutRequest).filter(UserWorkoutRequest.WorkoutID == w.ID).delete()
    db.delete(w)
    db.commit()
    db.close()

#tests the correct workout and response is made when the user requests a repeat workout. I have entered dummy data.
def test_create_request_repeat_workout_success():
    db = SessionLocal()

    w1 = workouts(Name="Athlete workout", Description="workout 1")
    w2 = workouts(Name="Athlete1 workout", Description="workout 2")
    db.add(w1)
    db.add(w2)
    db.commit()
    db.refresh(w1)
    db.refresh(w2)

    user = ensure_test_user(db)
    request1 = UserWorkoutRequest(UserID=user.ID, RequestType="repeat_workout", Status="Done", WorkoutID=w1.ID)
    request2 = UserWorkoutRequest(UserID=user.ID, RequestType="repeat_workout", Status="Done", WorkoutID=w2.ID)
    db.add(request1)
    db.add(request2) 
    db.commit()

    response = client.post("/users/requests", json={"request_type": "repeat_workout"}, headers=auth_header(db))
    assert response.status_code == 200
    data = response.json()
    assert data["Name"] == "Athlete1 workout"

    db.query(UserWorkoutRequest).delete()
    db.delete(w1)
    db.delete(w2)
    db.commit()
    db.close()

#tests the correct error is raised when the wrong workout is requested    
def test_create_request_error():
    db = SessionLocal()

    db.query(workouts).filter(workouts.Name == "Endurance Workout").delete()
    db.commit()

    response = client.post("/users/requests", json={"request_type": "upgrade_level"}, headers=auth_header(db))

    assert response.status_code == 404
    assert response.json()["detail"] == "Workout not found for request type"
    
    db.close()
    
#PROFILE.PY ROUTER FUNCTION TESTS

#tests the successful creation of user creating their profile with their profile details
def test_create_profile_success():
    db = SessionLocal()

    user = ensure_test_user(db)
    db.query(UserProfile).filter(UserProfile.UserID == user.ID).delete() #deletes so no errors come from user profile details already being there
    db.commit()

    profile_details = {
        "FullName": "Test User",
        "Age": 30,
        "Height": 175,                   
        "Weight": 72,                   
        "FitnessLevel": "Beginner",
        "Goal": "Lose weight",
        "InjuriesOrLimitations": "None"
    }

    response = client.post("/profile", json=profile_details, headers=auth_header(db))
    assert response.status_code == 200, response.json()
    data = response.json()
        
    assert data["FullName"] == "Test User"
    assert data["Age"] == 30
    assert data["HeightCM"] == 175
    assert data["WeightKG"] == 72
    assert data["FitnessLevel"] == "Beginner"
    assert data["Goal"] == "Lose weight"
    assert data["InjuriesOrLimitations"] == "None"

    db.query(UserProfile).filter(UserProfile.UserID == user.ID).delete()
    db.commit()
    db.close()

#tests the correct error is raised if the user tries to add a new profile when they have one already    
def test_create_profile_duplicate_user():
    db = SessionLocal()

    user = ensure_test_user(db)
    existing = UserProfile(
            UserID=user.ID, 
            FullName="Existing", 
            Age=25,
            HeightCM=170, 
            WeightKG=65, 
            FitnessLevel="Beginner",
            Goal="Stay fit", 
            InjuriesOrLimitations="None"
    )
    db.add(existing)
    db.commit()
    db.refresh(existing)

    additional_profile = {
        "FullName": "Another One",
        "Age": 26,
        "Height": 171,
        "Weight": 66,
        "FitnessLevel": "Intermediate",
        "Goal": "Build muscle",
        "InjuriesOrLimitations": ""
    }
    
    response = client.post("/profile", json=additional_profile , headers=auth_header(db))
    assert response.status_code == 400
    assert response.json()["detail"] == "User profile already exists."

    db.query(UserProfile).filter(UserProfile.UserID == user.ID).delete()
    db.commit()
    db.close()

#successfully returns the user's profile details when requested to see them    
def test_return_user_profile_details():
    db = SessionLocal()

    user = ensure_test_user(db)

    profile = UserProfile(
        UserID=user.ID,
        FullName="Test User",
        Age=30,
        HeightCM=175,
        WeightKG=72,
        FitnessLevel="Beginner",
        Goal="Lose weight",
        InjuriesOrLimitations="None",
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)

    response = client.get("/profile/summary", headers=auth_header(db))
    assert response.status_code == 200
    data = response.json()

    assert data["FullName"] == "Test User"
    assert data["Age"] == 30
    assert data["HeightCM"] == 175
    assert data["WeightKG"] == 72
    assert data["FitnessLevel"] == "Beginner"
    assert data["Goal"] == "Lose weight"
    assert data["InjuriesOrLimitations"] == "None"

    db.delete(profile)
    db.commit()
    db.close()

#successfully updates the user's profile when the user wants to update certain information
def test_update_profile_success():
    db = SessionLocal()

    user = ensure_test_user(db)
    profile = UserProfile(
        UserID=user.ID,
        FullName="Robert Smith",
        Age=29,
        HeightCM=170,
        WeightKG=70,
        FitnessLevel="Beginner",
        Goal="Start training",
        InjuriesOrLimitations="None",
    )
    db.add(profile)
    db.commit()
    db.refresh(profile)

    update_details = {
        "FullName": "Rob Smith",
        "Weight": 72,               
        "FitnessLevel": "Intermediate",
    }
    response = client.post("/profile/update-profile", json=update_details, headers=auth_header(db))

    assert response.status_code == 200
    data = response.json()
    
    assert data["FullName"] == "Rob Smith"
    assert data["WeightKG"] == 72
    assert data["FitnessLevel"] == "Intermediate"
    assert data["Age"] == 29
    assert data["HeightCM"] == 170

    db.delete(profile)
    db.commit()
    db.close()

#returns the correct error when wrong profile name is requested    
def test_update_profile_not_found_error():
    db = SessionLocal()

    user = ensure_test_user(db)
    db.query(UserProfile).filter(UserProfile.UserID == user.ID).delete()
    db.commit()

    profile = {"FullName": "Angela Smith"}
    response = client.post("/profile/update-profile", json=profile, headers=auth_header(db))

    assert response.status_code == 404
    assert response.json()["detail"] == "User profile not found"

    db.close()
    
#AUTH.PY ROUTER FUNCTION TESTS

#successfully tests the user login and authentication
def test_login_form_success():
    db = SessionLocal()

    email = "user@example.com"
    plain_pw = "password123"

    db.query(User).filter(User.Email == email).delete()
    db.commit()

    hashed_pw = pwd_context.hash(plain_pw)
    new_user = User(Email=email, HashedPassword=hashed_pw, IsActive=True)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    response = client.post("/login/form", data={"username": email, "password": plain_pw})

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    db.delete(new_user)
    db.commit()
    db.close()
    
#tests the correct error is raised once the user enters the wrong password
def test_login_form_wrong_password():
    db = SessionLocal()

    email = "test2@example.com"
    plain_pw = "password123"

    db.query(User).filter(User.Email == email).delete()
    db.commit()

    hashed_pw = pwd_context.hash(plain_pw)
    user = User(Email=email, HashedPassword=hashed_pw, IsActive=True)
    db.add(user)
    db.commit()
    db.refresh(user)

    response = client.post("/login/form", data={"username": email, "password": "wrongpass"})

    assert response.status_code == 403
    assert response.json()["detail"] == "Invalid Username or Password"

    db.delete(user)
    db.commit()
    db.close()

#similar test like the above but this is the user test route
def test_login_success():
    db = SessionLocal()

    email = "user@example.com"
    plain_pw = "password123"

    db.query(User).filter(User.Email == email).delete()
    db.commit()

    hashed_pw = pwd_context.hash(plain_pw)
    new_user = User(Email=email, HashedPassword=hashed_pw, IsActive=True)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    response = client.post("/login", json={"Email": email, "Password": plain_pw})

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

    db.delete(new_user)
    db.commit()
    db.close()

#tests the correct error is raised when the wrong password is entered    
def test_login_wrong_password():
    db = SessionLocal()

    email = "test2@example.com"
    plain_pw = "password123"

    db.query(User).filter(User.Email == email).delete()
    db.commit()

    hashed_pw = pwd_context.hash(plain_pw)
    user = User(Email=email, HashedPassword=hashed_pw, IsActive=True)
    db.add(user)
    db.commit()
    db.refresh(user)

    response = client.post("/login", json={"Email": email, "Password": "test1"})

    assert response.status_code == 403
    assert response.json()["detail"] == "Invalid Username or Password"

    db.delete(user)
    db.commit()
    db.close()

