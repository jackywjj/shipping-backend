from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class LoginForm(BaseModel):
    """
    登录Form
    """
    user_name: str
    user_password: str
    captcha_code: str
    captcha_value: str

    @field_validator('user_name')
    def user_name_not_empty(cls, v):
        """
        Validate user name
        """
        if len(v.strip()) == 0:
            raise ParamsError("用户名不能为空")
        return v

    @field_validator('user_password')
    def user_password_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("密码不能为空")
        return v

    @field_validator('captcha_code')
    def captcha_code_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("缺少参数")
        return v

    @field_validator('captcha_value')
    def captcha_value_not_empty(cls, v):
        if len(v.strip()) == 0:
            raise ParamsError("验证码不能为空")
        return v
