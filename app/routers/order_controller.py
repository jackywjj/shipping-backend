from fastapi import APIRouter

from app.constants.order_enum import OrderStatusEnum
from app.schemas.order_schema import OrderForm, OrderVo
from app.services.container_service import ContainerService
from app.services.order_service import OrderService

router = APIRouter(prefix="/api/orders", tags=['订单模块'])


@router.post("", summary='新增订单')
async def create_order(order_form: OrderForm):
    err = OrderService.create_order(order_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="订单创建成功")


@router.get("", summary='获取订单列表')
async def get_orders(page_number: int = 1, page_size: int = 10):
    result, err = OrderService.get_orders(page_number, page_size)
    orders = result['data']
    order_vo_list = []
    for order in orders:
        order_item_list = OrderService.get_order_item_list(order.id)
        order_vo = OrderVo()
        order_vo.id = order.id
        order_vo.customer_id = order.customer_id
        order_vo.route_id = order.route_id
        order_vo.ship_id = order.ship_id
        order_vo.departure_date = order.departure_date
        order_vo.order_status = order.order_status
        order_vo.order_item_list = order_item_list

        container_list = ContainerService.get_containers_by_order(order.id)
        order_vo.order_containers = container_list

        order_vo_list.append(order_vo)

    result['data'] = order_vo_list
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{order_id}", summary='根据ID获取订单')
async def get_order_by_id(order_id):
    result = OrderService.get_order_by_id(order_id)
    return dict(code=0, msg="", data=result)


@router.get("/{order_id}/pending", summary='根据ID更改订单状态为：PENDING 准备中')
async def update_order_pending(order_id):
    result = OrderService.update_order_by_id(order_id, OrderStatusEnum.PENDING.name)
    return dict(code=0, msg="", data=result)


@router.get("/{order_id}/shipped", summary='根据ID更改订单状态为：SHIPPED 运输中')
async def update_order_shipped(order_id):
    result = OrderService.update_order_by_id(order_id, OrderStatusEnum.SHIPPED.name)
    return dict(code=0, msg="", data=result)


@router.get("/{order_id}/delivered", summary='根据ID更改订单状态为：DELIVERED 已送达')
async def update_order_delivered(order_id):
    result = OrderService.update_order_by_id(order_id, OrderStatusEnum.DELIVERED.name)
    return dict(code=0, msg="", data=result)
