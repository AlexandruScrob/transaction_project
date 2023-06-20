from typing import Any

from fastapi import APIRouter

from core.settings import get_settings
from orders.serializers import OrderModel

router = APIRouter()
settings = get_settings()


# Mock of an Orders table from a DB
ORDERS: dict[int, dict[str, Any]] = {
    0: {"items": ["strawberries", "vanilla", "bread"], "total_price": 20},
    1: {"items": ["water", "pepsi"], "total_price": 5},
    2: {"items": ["doughnuts", "croissants", "chocolate"], "total_price": 5},
}


@router.get("/order/{order_id}", response_model=OrderModel | None)
def get_order(order_id: int):
    order = ORDERS.get(order_id)

    if order is not None:
        return OrderModel(order_id=order_id, items=order["items"], total_price=order["total_price"])

    return None


@router.post("/order", response_model=OrderModel)
@router.patch("/order", response_model=OrderModel)
def create_update_order(order_data: OrderModel):
    order_dict = order_data.dict(exclude={"order_id"})
    ORDERS[order_data.order_id] = order_dict
    return order_data


@router.delete("/order/{order_id}", response_model=None)
def delete_order(order_id: int):
    ORDERS.pop(order_id)
    return None
