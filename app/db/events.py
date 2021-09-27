from fastapi import FastAPI
from sqlalchemy import MetaData, Table, Column
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql.sqltypes import Integer, String

ENGINE = None
CONN = None
PAPERS = None


async def connect_to_db(app: FastAPI) -> None:
    pass


async def close_db_connection(app: FastAPI) -> None:
    pass
