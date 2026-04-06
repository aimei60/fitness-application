#initialises FastAPI, configures CORS, registers routers and includes 2 routes
from fastapi import FastAPI, Request, Response
from application.routers import workouts, user, user_request, auth, profile
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware  # use Starlette's proxy headers
from slowapi.middleware import SlowAPIMiddleware
from application.rate_limit import limiter
from starlette.responses import JSONResponse
import os
import secrets

app = FastAPI()

IS_PROD = os.getenv("ENV", "development").lower() in {"prod", "production"}
#Central cookie
COOKIE_DOMAIN = None

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
    response.headers["X-Content-Type-Options"] = "nosniff" #prevents browsers from guessing file types
    response.headers["Content-Security-Policy"] = "frame-ancestors 'none';" #stops my site being embeddeded in iframes
    
    if request.url.scheme == "https" and request.headers.get("host") in {"api.fitrequest.dev"}:
        #testing for 1 day first
        response.headers["Strict-Transport-Security"] = "max-age=86400; includeSubDomains"
    return response

# Add SlowAPI rate limiting (global default: 100/min/IP)
app.state.limiter = limiter

#the below doesnt limit browser's permission check requests
class SkipOptionsRateLimitMiddleware(SlowAPIMiddleware):
    async def dispatch(self, request, call_next):
        #if it's a browser request, skip rate limiting
        if request.method == "OPTIONS":
            return await call_next(request)

        #otherwise, apply normal rate limiting
        return await super().dispatch(request, call_next)

app.add_middleware(SkipOptionsRateLimitMiddleware)

#csrf route to create csrf token
@app.get("/api/csrf-token")
def get_csrf_token(response: Response):
    token = secrets.token_urlsafe(32)
    
    response.set_cookie(
        key="csrf_token",
        value=token,
        httponly=True,
        secure=IS_PROD,
        samesite="none" if IS_PROD else "lax",
        path="/",
        **({"domain": COOKIE_DOMAIN} if COOKIE_DOMAIN else {})
    )
    
    return {"csrfToken": token}

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
