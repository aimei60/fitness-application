#initialises FastAPI, configures CORS, registers routers and includes 2 routes

from fastapi import FastAPI, Request, Header, Cookie, HTTPException
from application.routers import workouts, user, user_request, auth, profile
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware  # use Starlette's proxy headers
from slowapi.middleware import SlowAPIMiddleware
from application.rate_limit import limiter
from starlette.responses import JSONResponse
import os

app = FastAPI()

#website under maintenance blocking login/sign up routes
MAINTENANCE_MODE = os.getenv("MAINTENANCE_MODE", "false").lower() == "true"
MAINTENANCE_MSG = os.getenv("MAINTENANCE_MSG", "Sign in is temporarily disabled for maintenance.")

@app.middleware("http")
async def maintenance_auth_gate(request: Request, call_next):
    if MAINTENANCE_MODE and request.url.path.startswith(("/login", "/signup")):
        return JSONResponse({"detail": MAINTENANCE_MSG}, status_code=503)
    return await call_next(request)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fitrequest.dev",
        "https://www.fitrequest.dev",
        "http://localhost:5173",
    ],
    allow_credentials=True,  # using cookies 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Make to see the real client IP when behind a proxy (Fly/Gunicorn/Uvicorn/etc.)
app.add_middleware(ProxyHeadersMiddleware, trusted_hosts="*")

# Security headers + HSTS (only on production HTTPS)
@app.middleware("http")
async def sec_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    
    if request.url.scheme == "https" and request.headers.get("host") in {"api.fitrequest.dev"}:
        #testing for 1 day first
        response.headers["Strict-Transport-Security"] = "max-age=86400; includeSubDomains"
    return response

# Add SlowAPI rate limiting (global default: 100/min/IP)
app.state.limiter = limiter

#Only add SlowAPI middleware if it's installed

class SkipOptionsSlowAPIMiddleware(SlowAPIMiddleware):
    async def dispatch(self, request, call_next):
        if request.method == "OPTIONS":
            # let CORSMiddleware handle the preflight and pass straight through
            return await call_next(request)
        return await super().dispatch(request, call_next)

app.add_middleware(SkipOptionsSlowAPIMiddleware)

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
