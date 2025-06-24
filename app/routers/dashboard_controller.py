from fastapi import APIRouter

from app.services.message_service import MessageService
from app.services.order_service import OrderService
from app.utils.response_json import response_success

router = APIRouter(prefix="/api/dashboard", tags=['Dashboard仪表盘'])


@router.get("", summary='Dashboard仪表盘')
async def get_overview():
    order_amount = OrderService.get_order_amount()
    message_list = MessageService.get_last_messages()
    order_chart = [{"order_date": "2025-05-27", "order_amount": 1}, {"order_date": "2025-05-26", "order_amount": 3},
                   {"order_date": "2025-05-25", "order_amount": 3}, {"order_date": "2025-05-24", "order_amount": 4},
                   {"order_date": "2025-05-23", "order_amount": 3}, {"order_date": "2025-05-22", "order_amount": 1},
                   {"order_date": "2025-05-21", "order_amount": 4}]
    data = {"order_amount": order_amount, "message_list": message_list, "order_chart": order_chart}
    return response_success(data)
