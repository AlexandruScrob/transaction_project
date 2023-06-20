from typing import Any, Type

from crud.models import Base, to_dict
from crud.engine import DBSession

DataObject = dict[str, Any]


class DBInterface:
    def __init__(self, db_class: Type[Base]):
        self.db_class = db_class

    def get_by_id(self, item_id: str) -> DataObject | None:
        session = DBSession()
        result = session.query(self.db_class).get(item_id)

        return None if result is None else to_dict(result)

    def create(self, data: DataObject) -> DataObject:
        session = DBSession()
        result = self.db_class(**data)
        session.add(result)
        session.commit()
        session.refresh(result)
        return to_dict(result)

    def read_all(self) -> list[DataObject]:
        session = DBSession()
        results = session.query(self.db_class).all()
        return [to_dict(r) for r in results]

    def delete(self, item_id: str) -> str | None:
        session = DBSession()
        result = session.query(self.db_class).get(item_id)

        if result is None:
            return None

        session.delete(result)
        session.commit()
        return item_id

    def update(self, item_id: str, data: DataObject) -> DataObject | None:
        session = DBSession()
        result = session.query(self.db_class).get(item_id)

        if result is None:
            return None

        for key, value in data.items():
            setattr(result, key, value)

        session.commit()
        session.refresh(result)
        return to_dict(result)
