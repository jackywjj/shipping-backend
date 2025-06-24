from typing import Any

from sqlalchemy import Column, String, BIGINT

from app.models import Base


class Container(Base):
    __tablename__ = "tbl_containers"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    order_id = Column(BIGINT, default=0, comment="所属订单ID")
    container_number = Column(String(30), comment="集装箱编号")
    type = Column(String(50), comment="集装箱类型")

    def __init__(self, order_id, container_number, type, **kwargs: Any):
        super().__init__(**kwargs)
        self.order_id = order_id
        self.container_number = container_number
        self.type = type
