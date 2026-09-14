from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from app.models.bookmark import Bookmark

class BookmarkRepository:
    def get(self, db: Session, user_id: int, repository_id: int):
        return db.scalar(select(Bookmark).where(Bookmark.user_id == user_id, Bookmark.repository_id == repository_id))
    def create(self, db: Session, user_id: int, repository_id: int):
        bookmark = Bookmark(user_id=user_id, repository_id=repository_id); db.add(bookmark); db.commit(); db.refresh(bookmark); return bookmark
    def delete(self, db: Session, bookmark: Bookmark):
        db.delete(bookmark); db.commit()
    def list_for_user(self, db: Session, user_id: int):
        return list(db.scalars(select(Bookmark).options(joinedload(Bookmark.repository)).where(Bookmark.user_id == user_id).order_by(Bookmark.created_at.desc())))
bookmark_repository = BookmarkRepository()
