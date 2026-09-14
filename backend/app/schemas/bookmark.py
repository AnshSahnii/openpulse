from pydantic import BaseModel
from app.schemas.repository import RepositoryResponse

class BookmarkResponse(BaseModel):
    id: int
    repository: RepositoryResponse
    model_config = {"from_attributes": True}
