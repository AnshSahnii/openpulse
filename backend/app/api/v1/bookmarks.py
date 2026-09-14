from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.dependencies import get_database, get_current_user
from app.schemas.bookmark import BookmarkResponse
from app.services.bookmark_service import bookmark_service

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])

@router.get("/", response_model=list[BookmarkResponse])
def list_bookmarks(db: Session = Depends(get_database), user=Depends(get_current_user)):
    return bookmark_service.list(db, user.id)

@router.post("/{repository_id}", response_model=BookmarkResponse, status_code=201)
def add_bookmark(repository_id: int, db: Session = Depends(get_database), user=Depends(get_current_user)):
    return bookmark_service.add(db, user.id, repository_id)

@router.delete("/{repository_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_bookmark(repository_id: int, db: Session = Depends(get_database), user=Depends(get_current_user)):
    bookmark_service.remove(db, user.id, repository_id)
