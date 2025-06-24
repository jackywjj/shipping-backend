from fastapi import APIRouter

from app.constants.schedule_enum import ScheduleStatusEnum, get_schedule_status_label
from app.excpetions.error_base import ErrorBase
from app.schemas.schedule_schema import ScheduleVo
from app.services.port_service import PortService
from app.services.route_service import RouteService
from app.services.schedule_service import ScheduleService
from app.services.ship_service import ShipService
from app.utils.response_json import response_error, response_success

router = APIRouter(prefix="/api/schedules", tags=['航运调度模块'])


@router.get("")
async def get_schedules(page_number: int = 1, page_size: int = 10):
    result, err = ScheduleService.get_schedules(page_number, page_size)
    schedule_list = []
    for schedule in result['data']:
        vo = ScheduleVo()
        vo.id = schedule.id
        vo.ship_id = schedule.ship_id

        ship = ShipService.get_ship_by_id(schedule.ship_id)
        vo.ship_name = ship.ship_name
        vo.ship_type = ship.ship_type
        vo.ship_capacity = ship.ship_capacity

        vo.route_id = schedule.route_id
        route = RouteService.get_route_by_id(schedule.route_id)
        origin_port = PortService.get_port_by_id(route.origin_port_id)
        vo.origin_port_id = origin_port.id
        vo.origin_port_name = origin_port.port_name

        destination_port = PortService.get_port_by_id(route.origin_port_id)
        vo.destination_port_id = destination_port.id
        vo.destination_port_name = destination_port.port_name

        vo.route_label = vo.origin_port_name + ' - ' + vo.destination_port_name

        vo.departure_time = schedule.departure_time
        vo.arrival_time = schedule.arrival_time
        vo.status = schedule.status
        vo.status_label = get_schedule_status_label(schedule.status)
        schedule_list.append(vo)

    result['data'] = schedule_list
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{schedule_id}")
async def get_schedule_by_id(schedule_id):
    result = ScheduleService.get_schedule_by_id(schedule_id)
    return dict(code=0, msg="", data=result)


@router.put("/{schedule_id}/in_progress")
async def update_schedule_info(schedule_id):
    result = ScheduleService.update_schedule_by_id(schedule_id, ScheduleStatusEnum.IN_PROGRESS.name)
    if result:
        return response_error(ErrorBase(code=500, msg="修改航运调度失败"))
    return response_success()


@router.put("/{schedule_id}/completed")
async def update_schedule_info(schedule_id):
    result = ScheduleService.update_schedule_by_id(schedule_id, ScheduleStatusEnum.COMPLETED.name)
    if result:
        return response_error(ErrorBase(code=500, msg="修改航运调度失败"))
    return response_success()
