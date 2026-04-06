import os
import httpx

TURNSTILE_SECRET_KEY = os.getenv("TURNSTILE_SECRET_KEY")

async def verify_turnstile(token: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://challenges.cloudflare.com/turnstile/v0/siteverify",
                data={
                    "secret": TURNSTILE_SECRET_KEY,
                    "response": token,
                },
                timeout=10,
            )

        result = response.json()
        return result.get("success", False)

    except Exception:
        return False