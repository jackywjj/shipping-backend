from typing import Any

from sqlalchemy import Column, String, BIGINT

from app.models import Base


class Port(Base):
    __tablename__ = "tbl_ports"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    port_code = Column(String(5), comment="港口Code")
    port_name = Column(String(50), comment="港口名称")
    country = Column(String(50), comment="国家")

    def __init__(self, port_code, port_name, country, **kwargs: Any):
        super().__init__(**kwargs)
        self.port_code = port_code
        self.port_name = port_name
        self.country = country
