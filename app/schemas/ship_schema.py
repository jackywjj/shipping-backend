from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class ShipForm(BaseModel):
    ship_name: str
    ship_type: str
    ship_capacity: int

    @field_validator('ship_name')
    def ship_name_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("船名不能为空")
        return v
