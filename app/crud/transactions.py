from uuid import uuid4
from typing import Any

from crud.interface import DBInterface
from transactions.serializers import TransactionModel


DataObject = dict[str, Any]


def get_transaction(transaction_id: str, transaction_interface: DBInterface) -> DataObject | None:
    return transaction_interface.get_by_id(transaction_id)


def get_all_transactions(transaction_interface: DBInterface) -> list[DataObject]:
    return transaction_interface.read_all()


def create_transaction(data: TransactionModel, transaction_interface: DBInterface) -> DataObject:
    data_dict = data.dict()
    data_dict["transaction_id"] = str(uuid4())
    data_dict["priority"] = data.priority.value
    return transaction_interface.create(data_dict)


def update_transaction(
    transaction_id: str, data: TransactionModel, transaction_interface: DBInterface
) -> DataObject | None:
    data_dict = data.dict()
    data_dict["priority"] = data.priority.value
    return transaction_interface.update(transaction_id, data=data_dict)


def delete_transaction(transaction_id: str, transaction_interface: DBInterface) -> str | None:
    return transaction_interface.delete(transaction_id)
