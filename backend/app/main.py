from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.config import settings
from app.core.error_handlers import openpulse_error_handler
from app.core.exceptions import OpenPulseError
from app.core.middleware import RequestTimingMiddleware
from app.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title=settings.app_name, version=settings.app_version, description="OpenPulse: discover, analyze and bookmark open-source repositories.", lifespan=lifespan)
app.add_middleware(RequestTimingMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=[settings.frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_exception_handler(OpenPulseError, openpulse_error_handler)
app.include_router(api_router, prefix=settings.api_prefix)

@app.get("/")
def root():
    return {"message": "Welcome to OpenPulse 🚀", "status": "running", "docs": "/docs"}
