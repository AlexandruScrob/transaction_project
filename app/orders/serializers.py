from pydantic import BaseModel, Field


class OrderModel(BaseModel):
    order_id: int
    items: list[str] = Field(default_factory=list)
    total_price: float
