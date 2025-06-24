from typing import Any

from sqlalchemy import Column, String, BIGINT, DATE

from app.constants.schedule_enum import ScheduleStatusEnum
from app.models import Base


class Schedule(Base):
    __tablename__ = "tbl_schedules"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    ship_id = Column(BIGINT, comment="船舶ID")
    route_id = Column(BIGINT, comment="航线ID")
    departure_time = Column(DATE, nullable=False, comment="出发时间")
    arrival_time = Column(DATE, nullable=False, comment="预计到达时间")
    status = Column(String(20), comment="状态")

    def __init__(self, ship_id, route_id, **kwargs: Any):
        super().__init__(**kwargs)
        self.ship_id = ship_id
        self.route_id = route_id
        self.status = ScheduleStatusEnum.SCHEDULED.name
