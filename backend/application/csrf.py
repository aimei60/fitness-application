from fastapi import Request, Header, HTTPException

#csrf token verification from frontend
def verify_csrf(request: Request, x_csrf_token: str = Header(None)):
    csrf_cookie = request.cookies.get("csrf_token")

    if not x_csrf_token or not csrf_cookie or x_csrf_token != csrf_cookie:
        raise HTTPException(status_code=403, detail="CSRF failed")
