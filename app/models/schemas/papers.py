from typing import List

from pydantic import BaseModel

from app.models.domain.papers import Paper


class PapersInResponse(BaseModel):
    papersNames: List[Paper]


class PaperInDatabase(BaseModel):
    __tablename__ = 'papers'

    paperName: str
    isUseful: str
    isComplicated: int
    readPercent: int
    description: str
