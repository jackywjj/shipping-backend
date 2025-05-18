from datetime import datetime
from typing import Any

from sqlalchemy import Column, String, INT, DATETIME, BIGINT

from app.models import Base


class Customer(Base):
    __tablename__ = "tbl_customers"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    company_name = Column(String(100), comment="公司名称")
    contact_name = Column(String(50), comment="联系人")
    company_phone = Column(String(20), comment="联系电话")
    company_email = Column(String(100), comment="邮箱")
    company_address = Column(String(255), comment="联系地址")
    created_at = Column(DATETIME, nullable=False, comment="创建时间")
    active = Column(INT, comment="删除标识")

    def __init__(self, company_name, contact_name, company_phone, company_email, company_address, **kwargs: Any):
        super().__init__(**kwargs)
        self.company_name = company_name
        self.contact_name = contact_name
        self.company_phone = company_phone
        self.company_email = company_email
        self.company_address = company_address
        self.created_at = datetime.now()
        self.active = 1
