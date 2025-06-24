from fastapi import APIRouter

from app.excpetions.error_base import ErrorBase
from app.schemas.ship_schema import ShipForm, UpdateShipForm
from app.services.ship_service import ShipService
from app.utils.response_json import response_success, response_error

router = APIRouter(prefix="/api/ships", tags=['船只信息模块'])


@router.post("")
async def create_ship(ship_form: ShipForm):
    err = ShipService.create_ship(ship_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="船只创建成功")


@router.get("")
async def get_ships(page_number: int = 1, page_size: int = 10):
    result, err = ShipService.get_ships(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/all")
async def get_all_ships():
    result, err = ShipService.get_all_ships()
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{ship_id}")
async def get_ship_by_id(ship_id):
    result = ShipService.get_ship_by_id(ship_id)
    return dict(code=0, msg="", data=result)


@router.put("/update")
async def update_ship_info(update_ship_form: UpdateShipForm):
    result = ShipService.update_ship_info(update_ship_form)
    if result:
        return response_error(ErrorBase(code=500, msg="修改船只信息失败"))
    return response_success()


@router.delete("/{ship_id}")
async def delete_ship(ship_id):
    result = ShipService.delete_ship_by_id(ship_id)
    return dict(code=0, msg="", data=result)
