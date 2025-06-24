from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class ShipForm(BaseModel):
    ship_name: str
    ship_type: str
    ship_capacity: int
    status: str

    @field_validator('ship_name')
    def ship_name_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("船名不能为空")
        return v


class UpdateShipForm(BaseModel):
    ship_id: int
    ship_name: str = None
    ship_type: str = None
    ship_capacity: int = 0
    status: str
