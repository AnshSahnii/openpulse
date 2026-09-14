from sqlalchemy.orm import Session
from app.core.cache import repo_cache
from app.integrations.github.client import github_client
from app.repositories.repository_repository import repository_repository

class RepositoryService:
    def get_repository(self, db: Session, owner: str, repo: str):
        key = f"repo:{owner.lower()}/{repo.lower()}"
        cached = repo_cache.get(key)
        data = cached or github_client.get_repository(owner, repo)
        if not cached: repo_cache.set(key, data)
        return repository_repository.upsert_from_github(db, data)
    def search_repositories(self, query: str, page: int = 1, per_page: int = 20):
        return github_client.search_repositories(query, page, per_page)
    def recent(self, db: Session, limit: int = 20):
        return repository_repository.list_recent(db, limit)
repository_service = RepositoryService()
