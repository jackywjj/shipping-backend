from pydantic import BaseModel, field_validator

from app.excpetions.params_exception import ParamsError


class MessageForm(BaseModel):
    message_title: str
    message_content: str

    @field_validator('message_title')
    def message_title_not_empty(cls, v):
        if v is None:
            raise ParamsError("标题不能为空")
        return v
