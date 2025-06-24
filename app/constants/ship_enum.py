import enum


class ShipTypeEnum(enum.Enum):
    CONTAINER_SHIP = "集装箱船（ContainerShip）"
    BULK_CARRIER = "散货船（BulkCarrier）"
    TANKER = "油轮（Tanker）"
    RO_RO_SHIP = "滚装船（RoRoShip）"
    GENERAL_CARGO_SHIP = "杂货船（GeneralCargo）"
    REEFER_SHIP = "冷藏船（ReeferShip）"


class ShipStatusEnum(enum.Enum):
    AVAILABLE = '可用'
    IN_TRANSIT = '作业中'
    MAINTENANCE = '维护中'
