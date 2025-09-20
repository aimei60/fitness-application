#initialises FastAPI, configures CORS, registers routers and includes 2 routes

from fastapi import FastAPI, Request
from application.routers import workouts, user, user_request, auth, profile
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()  

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fitrequest.dev",
        "https://www.fitrequest.dev",
        "http://localhost:5173",
    ],
    allow_credentials=False,   # not using cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

#makes sure https is used for my site
@app.middleware("http")
async def hsts_middleware(request: Request, call_next):
    response = await call_next(request)
    # only set on HTTPS production host
    if request.url.scheme == "https" and request.headers.get("host") in {
        "api.fitrequest.dev",
    }:
        # trialling 1 day first; later will use 6–12 months
        response.headers["Strict-Transport-Security"] = "max-age=86400; includeSubDomains"
    return response

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

