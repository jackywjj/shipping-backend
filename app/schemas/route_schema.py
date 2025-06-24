from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class RouteForm(BaseModel):
    origin_port_id: int
    destination_port_id: int
    estimated_days: int

    @field_validator('origin_port_id')
    def origin_port_id_not_empty(cls, v):
        if v is None:
            raise ParamsError("起始港口不能为空")
        return v

    @field_validator('destination_port_id')
    def destination_port_id_not_empty(cls, v):
        if v is None:
            raise ParamsError("目的港口不能为空")
        return v

    @field_validator('estimated_days')
    def estimated_days_not_empty(cls, v):
        if v is None:
            raise ParamsError("预计天数不能为空")
        return v


class UpdateRouteForm(BaseModel):
    route_id: int
    origin_port_id: int
    destination_port_id: int
    estimated_days: int


class RouteVo():
    route_id: int
    origin_port_id: int
    origin_port_code: str = None
    origin_port_name: str = None
    destination_port_id: int
    destination_port_code: str = None
    destination_port_name: str = None
    estimated_days: int
