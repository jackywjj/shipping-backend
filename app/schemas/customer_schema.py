from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class CustomerForm(BaseModel):
    company_name: str
    contact_name: str
    company_phone: str
    company_email: str
    company_address: str

    @field_validator('company_name')
    def company_name_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("公司名称不能为空")
        return v
