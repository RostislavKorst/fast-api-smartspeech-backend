from fastapi import APIRouter
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql.sqltypes import Integer, String

from app.core.config import DATABASE_URL
from app.models.domain.papers import Paper
from app.models.schemas.papers import PapersInResponse

router = APIRouter()


@router.post("", response_model=Paper, name="papers:post-new-paper")
async def add_new_paper(paper: Paper) -> Paper:
    ENGINE = create_engine(DATABASE_URL)
    CONN = ENGINE.connect()
    meta = MetaData()
    PAPERS = Table('papers_new2', meta,
                   Column('paperName', String(255), primary_key=True),
                   Column('isUseful', String(255)),
                   Column('isComplicated', Integer),
                   Column('readPercent', Integer),
                   Column('description', String(255)))
    try:
        PAPERS.create(ENGINE)
    except OperationalError:
        pass
    finally:
        print(CONN.execute(PAPERS.insert().values(paperName=paper.paperName,
                                                  isUseful=paper.isUseful,
                                                  isComplicated=paper.isComplicated,
                                                  readPercent=paper.readPercent,
                                                  description=paper.description)))
        CONN.close()
        ENGINE.dispose()

        return Paper(paperName=paper.paperName,
                     isUseful=paper.isUseful,
                     isComplicated=paper.isComplicated,
                     readPercent=paper.readPercent,
                     description=paper.description)


@router.get("", response_model=PapersInResponse, name="papers:get-all-papers")
async def get_all_papers() -> PapersInResponse:
    ENGINE = create_engine(DATABASE_URL)
    CONN = ENGINE.connect()
    meta = MetaData()
    PAPERS = Table('papers_new2', meta,
                   Column('paperName', String(255), primary_key=True),
                   Column('isUseful', String(255)),
                   Column('isComplicated', Integer),
                   Column('readPercent', Integer),
                   Column('description', String(255)))
    try:
        PAPERS.create(ENGINE)
    except OperationalError:
        pass
    finally:

        papers_list_from_response = CONN.execute(PAPERS.select()).fetchall()

        CONN.close()
        ENGINE.dispose()

        final_list_of_papers = list()

        for paperName, isUseful, isComplicated, readPercent, description in papers_list_from_response:
            final_list_of_papers.append(Paper(paperName=paperName,
                                              isUseful=isUseful,
                                              isComplicated=isComplicated,
                                              readPercent=readPercent,
                                              description=description))

        return PapersInResponse(papersNames=final_list_of_papers)
