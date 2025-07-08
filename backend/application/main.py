from fastapi import FastAPI
from .routers import workouts, user, user_request, auth

app = FastAPI()  

app.include_router(workouts.router)
app.include_router(user.router)
app.include_router(user_request.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Fitness Application"}