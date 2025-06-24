from typing import List

from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class OrderItemForm(BaseModel):
    order_id: int
    description: str = ''
    quantity: int = 0
    weight: str = ''
    volume: str = ''


class OrderForm(BaseModel):
    customer_id: int
    route_id: int
    ship_id: int
    departure_date: str
    order_status: str
    order_items: List[OrderItemForm] = []

    @field_validator('customer_id')
    def customer_id_not_empty(cls, v):
        if v is None:
            raise ParamsError("客户ID不能为空")
        return v


class OrderItemVo():
    order_id: int
    description: str = ''
    quantity: int = 0
    weight: str = ''
    volume: str = ''


class OrderContainerVo():
    container_id: int
    order_id: int
    container_number: str = ''
    type: str = ''


class OrderVo():
    id: int
    customer_id: int
    route_id: int
    ship_id: int
    departure_date: str
    order_status: str
    order_items: List[OrderItemVo] = []
    order_containers: List[OrderContainerVo] = []
