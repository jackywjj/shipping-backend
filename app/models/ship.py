from typing import Any

from sqlalchemy import Column, String, BIGINT, INT

from app.constants.ship_enum import ShipStatusEnum
from app.models import Base


class Ship(Base):
    __tablename__ = "tbl_ships"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    ship_name = Column(String(50), comment="船名")
    ship_type = Column(String(50), comment="船舶类型")
    ship_capacity = Column(INT, default=0, comment="载重吨")
    status = Column(String(20), comment="当前状态")
    active = Column(INT, comment="删除标识")

    def __init__(self, ship_name, ship_type, ship_capacity, **kwargs: Any):
        super().__init__(**kwargs)
        self.ship_name = ship_name
        self.ship_type = ship_type
        self.ship_capacity = ship_capacity
        self.status = ShipStatusEnum.AVAILABLE.name
        self.active = 1
