from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class UserForm(BaseModel):
    user_name: str
    user_password: str

    @field_validator('user_name')
    def user_name_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("用户名不能为空")
        return v


class UpdateForm(BaseModel):
    user_id: int
    user_password: str = None
    user_name: str = None
