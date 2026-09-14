from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions import OpenPulseError

def openpulse_error_handler(request: Request, exc: OpenPulseError):
    return JSONResponse(status_code=400, content={"detail": str(exc)})
