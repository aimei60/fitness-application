from fastapi import FastAPI
from .routers import workouts, user

app = FastAPI()  

app.include_router(workouts.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Fitness Application"}