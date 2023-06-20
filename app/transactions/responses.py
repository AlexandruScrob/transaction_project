from pydantic import BaseModel, Field


class TransactionNotFound(BaseModel):
    response_message: str = Field(alias="responseMessage", default="Transaction not found")

    class Config:
        allow_population_by_field_name = True


class TransactionResponse(BaseModel):
    transaction_id: str = Field(alias="transactionId")
    description: str | None
    price: float
    priority: int

    class Config:
        allow_population_by_field_name = True
