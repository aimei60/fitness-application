#confirms request came from frontend
from fastapi import Header, Cookie, HTTPException

#CSRF verify helper (use on POST/PUT/PATCH/DELETE)
def verify_csrf(x_csrf_token: str = Header(None), csrf_token: str = Cookie(None)):
    if not x_csrf_token or not csrf_token or x_csrf_token != csrf_token:
        raise HTTPException(status_code=403, detail="CSRF failed")