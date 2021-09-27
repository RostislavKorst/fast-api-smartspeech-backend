from pydantic import BaseModel
from typing import List

from app.models.domain.papers import Paper


class PapersInResponse(BaseModel):
    papersNames: List[Paper]
