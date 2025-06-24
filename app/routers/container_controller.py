from fastapi import APIRouter

from app.excpetions.error_base import ErrorBase
from app.schemas.container_schema import ContainerForm, UpdateContainerForm
from app.services.container_service import ContainerService
from app.utils.response_json import response_error, response_success

router = APIRouter(prefix="/api/containers", tags=['集装箱模块'])


@router.post("")
async def create_container(container_form: ContainerForm):
    err = ContainerService.create_container(container_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="集装箱创建成功")


@router.get("/{order_id}/containers", summary='获取订单关联的集装箱列表')
async def get_order_container_list(order_id):
    result = ContainerService.get_containers_by_order(order_id)
    return dict(code=0, msg="", data=result)


@router.put("/update")
async def update_container_info(update_container_form: UpdateContainerForm):
    result = ContainerService.update_container_info(update_container_form)
    if result:
        return response_error(ErrorBase(code=500, msg="修改集装箱失败"))
    return response_success()


@router.delete("/{container_id}")
async def delete_container(container_id):
    result = ContainerService.delete_container_by_id(container_id)
    return dict(code=0, msg="", data=result)
