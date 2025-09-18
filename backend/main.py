#initialises FastAPI, configures CORS, registers routers and includes 2 routes

from fastapi import FastAPI
from application.routers import workouts, user, user_request, auth, profile
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()  

origins = [
    os.getenv("FRONTEND_PREVIEW", "http://localhost:5173"), 
    os.getenv("FRONTEND_PRODUCTION", "https://frontend.vercel.app"),
    os.getenv("DOMAIN", "https://domainname.com"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o for o in origins if o], #cleans up urls by removing anything empty None or ""
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

@app.get("/health") #health check
def health(): 
    return {"ok": True}