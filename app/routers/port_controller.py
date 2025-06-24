from fastapi import APIRouter
from starlette.requests import Request

from app.excpetions.error_base import ErrorBase
from app.schemas.port_schema import PortForm, UpdatePortForm
from app.services.port_service import PortService
from app.utils.response_json import response_success, response_error

router = APIRouter(prefix="/api/ports", tags=['港口信息模块'])


@router.post("")
async def create_port(port_form: PortForm):
    err = PortService.create_port(port_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="港口创建成功")


@router.get("")
async def get_ports(request: Request, page_number: int = 1, page_size: int = 10):
    result, err = PortService.get_ports(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{port_id}")
async def get_port_by_id(request: Request, port_id):
    result = PortService.get_port_by_id(port_id)
    return dict(code=0, msg="", data=result)


@router.put("/update")
async def update_port_info(request: Request, update_port_form: UpdatePortForm):
    result = PortService.update_port_info(update_port_form)
    if result:
        return response_error(ErrorBase(code=500, msg="修改港口信息失败"))
    return response_success()


@router.delete("/{port_id}")
async def delete_port(request: Request, port_id):
    result = PortService.delete_port_by_id(port_id)
    return dict(code=0, msg="", data=result)
