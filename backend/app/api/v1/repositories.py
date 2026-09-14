from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.dependencies import get_database, get_current_user
from app.schemas.repository import RepositoryResponse
from app.services.repository_service import repository_service

router = APIRouter(prefix="/repositories", tags=["Repositories"])

@router.get("/search")
def search_repositories(q: str = Query(..., min_length=1), page: int = Query(1, ge=1), per_page: int = Query(20, ge=1, le=100)):
    return repository_service.search_repositories(q, page, per_page)

@router.get("/recent", response_model=list[RepositoryResponse])
def recent_repositories(limit: int = Query(20, ge=1, le=100), db: Session = Depends(get_database)):
    return repository_service.recent(db, limit)

@router.get("/{owner}/{repo}", response_model=RepositoryResponse)
def get_repository(owner: str, repo: str, db: Session = Depends(get_database), user=Depends(get_current_user)):
    repository = repository_service.get_repository(db, owner, repo)
    return repository
