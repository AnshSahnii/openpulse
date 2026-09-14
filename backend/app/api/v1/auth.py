from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_database, get_current_user
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse
from app.services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=TokenResponse, status_code=201)
def register(payload: RegisterRequest, db: Session = Depends(get_database)):
    user = auth_service.register(db, payload)
    return {"access_token": __import__("app.core.security", fromlist=["create_access_token"]).create_access_token(user.id), "token_type": "bearer", "user": user}

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_database)):
    user, token = auth_service.login(db, payload)
    return {"access_token": token, "token_type": "bearer", "user": user}

@router.get("/me", response_model=UserResponse)
def me(user=Depends(get_current_user)):
    return user
