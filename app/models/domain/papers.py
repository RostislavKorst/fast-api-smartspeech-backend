from pydantic import BaseModel


class Paper(BaseModel):
    paperName: str
    isUseful: str
    isComplicated: int
    readPercent: int
    description: str
