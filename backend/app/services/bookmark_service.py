from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories.bookmark_repository import bookmark_repository
from app.repositories.repository_repository import repository_repository

class BookmarkService:
    def add(self, db: Session, user_id: int, repository_id: int):
        repo = repository_repository.get_by_id(db, repository_id)
        if not repo: raise HTTPException(status_code=404, detail="Repository not found")
        if bookmark_repository.get(db, user_id, repository_id): raise HTTPException(status_code=409, detail="Repository already bookmarked")
        return bookmark_repository.create(db, user_id, repository_id)
    def remove(self, db: Session, user_id: int, repository_id: int):
        bookmark = bookmark_repository.get(db, user_id, repository_id)
        if not bookmark: raise HTTPException(status_code=404, detail="Bookmark not found")
        bookmark_repository.delete(db, bookmark)
    def list(self, db: Session, user_id: int):
        return bookmark_repository.list_for_user(db, user_id)
bookmark_service = BookmarkService()
