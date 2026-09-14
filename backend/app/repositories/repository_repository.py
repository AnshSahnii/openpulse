from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.repository import Repository

class RepositoryRepository:
    def get_by_full_name(self, db: Session, full_name: str):
        return db.scalar(select(Repository).where(Repository.full_name == full_name))
    def get_by_id(self, db: Session, repository_id: int):
        return db.get(Repository, repository_id)
    def upsert_from_github(self, db: Session, data: dict):
        repo = self.get_by_full_name(db, data["full_name"])
        values = {
            "github_id": data.get("id"), "full_name": data["full_name"], "owner": data["owner"]["login"],
            "name": data["name"], "description": data.get("description"), "html_url": data.get("html_url"),
            "language": data.get("language"), "stars": data.get("stargazers_count", 0),
            "forks": data.get("forks_count", 0), "open_issues": data.get("open_issues_count", 0),
        }
        if repo:
            for key, value in values.items(): setattr(repo, key, value)
        else:
            repo = Repository(**values); db.add(repo)
        db.commit(); db.refresh(repo); return repo
    def list_recent(self, db: Session, limit: int = 20):
        return list(db.scalars(select(Repository).order_by(Repository.stars.desc()).limit(limit)))
repository_repository = RepositoryRepository()
