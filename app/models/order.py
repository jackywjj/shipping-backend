from datetime import datetime
from typing import Any

from sqlalchemy import Column, BIGINT, INT, DATETIME, DATE, String

from app.constants.order_enum import OrderStatusEnum
from app.models import Base


class Order(Base):
    __tablename__ = "tbl_orders"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    customer_id = Column(INT, comment="客户ID")
    route_id = Column(INT, comment="所选航线")
    ship_id = Column(INT, comment="分配船舶")
    order_date = Column(DATETIME, nullable=False, comment="下单日期")
    departure_date = Column(DATE, nullable=False, comment="出发日期")
    order_status = Column(String(10), comment="状态")

    def __init__(self, customer_id, route_id, ship_id, departure_date, **kwargs: Any):
        super().__init__(**kwargs)
        self.customer_id = customer_id
        self.route_id = route_id
        self.ship_id = ship_id
        self.order_date = datetime.now()
        self.departure_date = departure_date
        self.order_status = OrderStatusEnum.WAIT_FOR_ORDER.name


class OrderItem(Base):
    __tablename__ = "tbl_order_items"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    order_id = Column(INT, comment="订单ID")
    description = Column(String(512), comment="货物描述")
    quantity = Column(INT, comment="数量")
    weight = Column(String(50), comment="总重（吨）")
    volume = Column(String(50), comment="总体积（立方米）")

    def __init__(self, order_id, description, quantity, weight, volume, **kwargs: Any):
        super().__init__(**kwargs)
        self.order_id = order_id
        self.description = description
        self.quantity = quantity
        self.weight = weight
        self.volume = volume
