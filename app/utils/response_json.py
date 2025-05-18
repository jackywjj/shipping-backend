from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.excpetions.error_base import ErrorBase


class RespJsonBase(BaseModel):
    code: int
    msg: str
    data: dict | list


def response_success(data: dict | list | str = None):
    """ 接口成功返回 """
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 0,
            'msg': '操作成功',
            'data': jsonable_encoder(data) or {}
        }
    )


def response_error(error: ErrorBase, *, data: dict | list | str = None, status_code: int = status.HTTP_200_OK):
    """ 错误接口返回 """
    return JSONResponse(
        status_code=status_code,
        content={
            'code': error.code,
            'msg': error.msg,
            'data': data or {}
        }
    )
