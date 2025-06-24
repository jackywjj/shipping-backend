from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class PortForm(BaseModel):
    port_code: str
    port_name: str
    country: str

    @field_validator('port_code')
    def port_code_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("港口Code不能为空")
        return v

    @field_validator('port_name')
    def port_name_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("港口名称不能为空")
        return v

    @field_validator('country')
    def country_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("国家不能为空")
        return v


class UpdatePortForm(BaseModel):
    port_id: int
    port_code: str = None
    port_name: str = None
    country: str = None
