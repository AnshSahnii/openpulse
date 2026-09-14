import httpx
from app.config import settings
from app.core.exceptions import GitHubError
from app.integrations.github.constants import GITHUB_API_BASE

class GitHubClient:
    def __init__(self):
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "OpenPulse"}
        if settings.github_token:
            headers["Authorization"] = f"Bearer {settings.github_token}"
        self.client = httpx.Client(base_url=GITHUB_API_BASE, timeout=20, follow_redirects=True, headers=headers)

    def get_repository(self, owner: str, repo: str):
        response = self.client.get(f"/repos/{owner}/{repo}")
        if response.status_code == 404:
            raise GitHubError("Repository not found on GitHub")
        if response.status_code == 403:
            raise GitHubError("GitHub API rate limit or access restriction")
        try:
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise GitHubError(f"GitHub request failed: {exc}") from exc
        return response.json()

    def search_repositories(self, query: str, page: int = 1, per_page: int = 20):
        response = self.client.get("/search/repositories", params={"q": query, "page": page, "per_page": per_page, "sort": "stars", "order": "desc"})
        if response.status_code == 403:
            raise GitHubError("GitHub API rate limit or access restriction")
        try:
            response.raise_for_status()
        except httpx.HTTPError as exc:
            raise GitHubError(f"GitHub search failed: {exc}") from exc
        return response.json()

github_client = GitHubClient()
