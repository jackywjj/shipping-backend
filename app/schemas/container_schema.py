from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class ContainerForm(BaseModel):
    order_id: int
    container_number: str
    type: int

    @field_validator('container_number')
    def container_number_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("集装箱编号不能为空")
        return v


class UpdateContainerForm(BaseModel):
    order_id: int
    container_number: str = None
    type: int = 0
