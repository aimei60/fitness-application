#initialises FastAPI, configures CORS, registers routers and includes 2 routes

from fastapi import FastAPI, Request, Header, Cookie, HTTPException
from application.routers import workouts, user, user_request, auth, profile
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from slowapi.middleware import SlowAPIMiddleware
from application.rate_limit import limiter
 
app = FastAPI(middleware=[Middleware(ProxyHeadersMiddleware, trusted_hosts=["*"])])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://fitrequest.dev",
        "https://www.fitrequest.dev",
        "http://localhost:5173",
    ],
    allow_credentials=True, #using cookies
    allow_methods=["GET","POST","PUT","PATCH","DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "X-CSRF-Token", "Accept"],
)

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
app.add_middleware(SlowAPIMiddleware)

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

