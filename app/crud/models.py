from typing import Any
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy import Column

Base = declarative_base()


def to_dict(obj) -> dict[str, Any]:
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


class DBTransaction(Base):
    __tablename__ = "transaction"
    transaction_id = Column(String(250), primary_key=True)
    description = Column(String(250), nullable=True)
    price = Column(Float, nullable=False)
    priority = Column(Integer, nullable=False)
