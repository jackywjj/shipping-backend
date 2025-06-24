from typing import Any

from sqlalchemy import Column, BIGINT, INT

from app.models import Base


class Route(Base):
    __tablename__ = "tbl_routes"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    origin_port_id = Column(INT, comment="起始港口")
    destination_port_id = Column(INT, comment="目的港口")
    estimated_days = Column(INT, comment="预计天数")

    def __init__(self, origin_port_id, destination_port_id, estimated_days, **kwargs: Any):
        super().__init__(**kwargs)
        self.origin_port_id = origin_port_id
        self.destination_port_id = destination_port_id
        self.estimated_days = estimated_days
