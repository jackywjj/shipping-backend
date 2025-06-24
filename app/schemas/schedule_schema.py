class ScheduleVo():
    id: int
    ship_id: int
    ship_name: str
    ship_type: str
    ship_capacity: int

    route_id: int
    route_label: str
    origin_port_id: int
    origin_port_name: str
    destination_port_id: int
    destination_port_name: str
    estimated_days: int

    departure_time: str
    arrival_time: str
    status: int
    status_label: str
