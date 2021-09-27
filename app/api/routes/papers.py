from fastapi import APIRouter

from app.models.domain.papers import Paper
from app.models.schemas.papers import PapersInResponse

router = APIRouter()


@router.post("", response_model=Paper, name="papers:post-new-paper")
async def add_new_paper(paper: Paper) -> Paper:
    return Paper(paperName='Time-series',
                 isUseful='да',
                 isComplicated=6,
                 readPercent=90,
                 description='Хорошая работа')


@router.get("", response_model=PapersInResponse, name="papers:get-all-papers")
async def get_all_papers() -> PapersInResponse:
    return PapersInResponse(papersNames=[Paper(paperName='Time-series',
                                               isUseful='да',
                                               isComplicated=6,
                                               readPercent=90,
                                               description='Хорошая работа'),
                                         Paper(paperName='Time-series-2',
                                               isUseful='да',
                                               isComplicated=6,
                                               readPercent=90,
                                               description='Хорошая работа')
                                         ])
