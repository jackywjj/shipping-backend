import enum


class ShipTypeEnum(enum.Enum):
    available = 'available'
    in_transit = 'in_transit'
    maintenance = 'maintenance'
