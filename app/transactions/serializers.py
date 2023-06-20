from enum import Enum
from pydantic import BaseModel, validator


class TransactionPriority(Enum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2


class TransactionModel(BaseModel):
    description: str | None
    price: float
    priority: TransactionPriority

    @validator("price")
    def validate_price(cls, v) -> float:  # pylint: disable=no-self-argument
        if v < 0:
            raise ValueError("Price has to be a positive number")
        return v
