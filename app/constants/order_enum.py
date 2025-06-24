from enum import Enum


class OrderStatusEnum(Enum):
    WAIT_FOR_ORDER = '等待下单'
    PENDING = '准备中'
    SHIPPED = '运输中'
    DELIVERED = '已送达'
