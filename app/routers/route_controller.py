from fastapi import APIRouter
from starlette.requests import Request

from app.excpetions.error_base import ErrorBase
from app.schemas.route_schema import RouteForm, UpdateRouteForm
from app.services.route_service import RouteService
from app.utils.response_json import response_success, response_error

router = APIRouter(prefix="/api/routes", tags=['航线信息模块'])


@router.post("")
async def create_route(route_form: RouteForm):
    err = RouteService.create_route(route_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="航线创建成功")


@router.get("")
async def get_routes(page_number: int = 1, page_size: int = 10):
    result, err = RouteService.get_routes(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/all", summary="获取所有航线")
async def get_routes():
    result, err = RouteService.get_all_routes()
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{route_id}")
async def get_route_by_id(request: Request, route_id):
    result = RouteService.get_route_by_id(route_id)
    return dict(code=0, msg="", data=result)


@router.put("/update")
async def update_route_info(request: Request, update_route_form: UpdateRouteForm):
    result = RouteService.update_route_info(update_route_form)
    if result:
        return response_error(ErrorBase(code=500, msg="修改航线信息失败"))
    return response_success()


@router.delete("/{route_id}")
async def delete_route(request: Request, route_id):
    result = RouteService.delete_route_by_id(route_id)
    return dict(code=0, msg="", data=result)
