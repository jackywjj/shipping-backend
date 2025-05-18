from datetime import datetime
from typing import Any

from sqlalchemy import Column, String, DATETIME, BIGINT, INT

from app.models import Base


class User(Base):
    __tablename__ = "tbl_users"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    user_name = Column(String(50), unique=True, index=True, comment="用户名")
    user_password = Column(String(50), unique=False, comment="用户密码")
    created_at = Column(DATETIME, nullable=False, comment="创建时间")
    active = Column(INT, comment="删除标识")

    def __init__(self, user_name, user_password, **kwargs: Any):
        super().__init__(**kwargs)
        self.user_name = user_name
        self.user_password = user_password
        self.created_at = datetime.now()
        self.active = 1
