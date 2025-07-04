from fastapi import FastAPI
from .routers import workouts

app = FastAPI()  

app.include_router(workouts.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Fitness Application"}