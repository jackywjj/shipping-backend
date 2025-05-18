from datetime import datetime
from typing import Any

from sqlalchemy import Column, INT, DATETIME, BIGINT

from app.models import Base


class CustomerTransactionRecord(Base):
    __tablename__ = "tbl_customer_transaction_records"

    id = Column(BIGINT, primary_key=True, comment="自增ID")
    customer_id = Column(BIGINT, default=0, comment="客户ID")
    transaction_type = Column(BIGINT, default=1, comment="交易类型")
    transaction_amount = Column(BIGINT, comment="交易金额")
    transaction_time = Column(DATETIME, nullable=False, comment="交易时间")
    active = Column(INT, comment="删除标识")

    def __init__(self, customer_id, transaction_type, transaction_amount, transaction_time, **kwargs: Any):
        super().__init__(**kwargs)
        self.customer_id = customer_id
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_time = datetime.now()
        self.active = 1
