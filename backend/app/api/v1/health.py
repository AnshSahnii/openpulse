from fastapi import APIRouter
from sqlalchemy import text
from app.database import engine

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/")
def health_check():
    return {"status": "healthy", "service": "OpenPulse API"}

@router.get("/db")
def database_health():
    try:
        with engine.connect() as connection: connection.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as exc:
        return {"status": "degraded", "database": "unavailable", "error": str(exc)}
