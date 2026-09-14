from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import create_access_token, hash_password, verify_password
from app.repositories.user_repository import user_repository
from app.schemas.auth import LoginRequest, RegisterRequest

class AuthService:
    def register(self, db: Session, payload: RegisterRequest):
        if user_repository.exists(db, payload.username, payload.email):
            raise HTTPException(status_code=409, detail="Username or email already registered")
        return user_repository.create(db, payload.username, payload.email, hash_password(payload.password))
    def login(self, db: Session, payload: LoginRequest):
        user = user_repository.get_by_username(db, payload.username)
        if not user or not verify_password(payload.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
        return user, create_access_token(user.id)
auth_service = AuthService()
