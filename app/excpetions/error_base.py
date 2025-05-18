from pydantic import BaseModel


class ErrorBase(BaseModel):
    code: int
    msg: str = ""
