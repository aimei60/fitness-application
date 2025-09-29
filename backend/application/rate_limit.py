#sets up rate limiting for API to prevent abuse e.g. DDoS attacks or brute-force attempts

from slowapi import Limiter
from slowapi.util import get_remote_address

# Global default: 100 requests/min per IP
limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])