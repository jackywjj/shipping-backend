from datetime import datetime
from typing import Any

from sqlalchemy import Column, BIGINT, INT, String, DATETIME

from app.models import Base


class Message(Base):
    __tablename__ = "tbl_messages"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    message_title = Column(String(200), comment="标题")
    message_content = Column(String(1024), comment="内容")
    sent_at = Column(DATETIME, nullable=False, comment="创建时间")
    active = Column(INT, comment="删除标识")

    def __init__(self, message_title, message_content, **kwargs: Any):
        super().__init__(**kwargs)
        self.message_title = message_title
        self.message_content = message_content
        self.sent_at = datetime.now()
        self.active = 1
