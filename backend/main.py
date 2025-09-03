import sys
print("sys.path =", sys.path)

from fastapi import FastAPI
from .application.routers import workouts, user, user_request, auth, profile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()  

origins = [
    "http://localhost:5173", #react  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,  #change to true if planning to use cookies
    allow_methods=["*"],
    allow_headers=["*"],    
)

app.include_router(workouts.router)
app.include_router(user.router)
app.include_router(user_request.router)
app.include_router(auth.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Fitness Application"}