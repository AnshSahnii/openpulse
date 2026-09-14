from datetime import datetime, timedelta, timezone
import hashlib
import hmac
import jwt
from app.config import settings

ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    salt = hashlib.sha256(f"{settings.jwt_secret}:{password}".encode()).hexdigest()[:32]
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 120_000).hex()
    return f"pbkdf2$120000${salt}${digest}"

def verify_password(password: str, encoded: str) -> bool:
    try:
        _, iterations, salt, expected = encoded.split("$", 3)
        actual = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), int(iterations)).hex()
        return hmac.compare_digest(actual, expected)
    except (ValueError, TypeError):
        return False

def create_access_token(user_id: int) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": str(user_id), "iat": now, "exp": now + timedelta(minutes=settings.jwt_expire_minutes)}
    return jwt.encode(payload, settings.jwt_secret, algorithm=ALGORITHM)

def decode_access_token(token: str) -> dict:
    try:
        return jwt.decode(token, settings.jwt_secret, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="Invalid or expired token")
