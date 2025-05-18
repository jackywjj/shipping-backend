from fastapi import APIRouter
from starlette.requests import Request

from app.utils.response_json import response_success

router = APIRouter(prefix="/api/dashboard", tags=['Dashboard'])


@router.get("")
async def get_overview(request: Request):
    device_amount = 1
    birth_amount = 2
    wean_amount = 3
    data = {"device_amount": device_amount, "birth_amount": birth_amount, "wean_amount": wean_amount}
    return response_success(data)
