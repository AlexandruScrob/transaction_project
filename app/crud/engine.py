from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Column, Integer, String, Float, Table
from sqlalchemy_utils import database_exists, create_database
from crud.models import Base


engine: Engine = None  # type: ignore
DBSession = sessionmaker()
meta = MetaData()


# Note: Recreate if lost table
transactions = Table(
    "transaction",
    meta,
    Column("transaction_id", String, primary_key=True),
    Column("description", String),
    Column("price", Float),
    Column("priority", Integer),
)


def init_db(file: str):
    engine = create_engine(file)

    Base.metadata.bind = engine
    DBSession.configure(bind=engine)

    if not database_exists(engine.url):
        create_database(engine.url)

    meta.create_all(engine)
