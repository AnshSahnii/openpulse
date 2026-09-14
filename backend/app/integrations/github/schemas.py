from pydantic import BaseModel

class GitHubOwner(BaseModel):
    login: str

class GitHubRepository(BaseModel):
    id: int
    name: str
    full_name: str
    description: str | None = None
    html_url: str
    language: str | None = None
    stargazers_count: int = 0
    forks_count: int = 0
    open_issues_count: int = 0
    owner: GitHubOwner
