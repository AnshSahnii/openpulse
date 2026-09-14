from sqlalchemy import or_, select
from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def get_by_username(self, db: Session, username: str):
        return db.scalar(select(User).where(User.username == username))
    def get_by_email(self, db: Session, email: str):
        return db.scalar(select(User).where(User.email == email))
    def create(self, db: Session, username: str, email: str, hashed_password: str):
        user = User(username=username, email=email, hashed_password=hashed_password)
        db.add(user); db.commit(); db.refresh(user); return user
    def exists(self, db: Session, username: str, email: str):
        return db.scalar(select(User).where(or_(User.username == username, User.email == email))) is not None
user_repository = UserRepository()
