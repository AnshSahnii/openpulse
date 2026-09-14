from pydantic import BaseModel

class RepositoryResponse(BaseModel):
    id: int
    full_name: str
    owner: str
    name: str
    description: str | None = None
    html_url: str | None = None
    language: str | None = None
    stars: int
    forks: int
    open_issues: int
    bookmarked: bool = False
    model_config = {"from_attributes": True}
