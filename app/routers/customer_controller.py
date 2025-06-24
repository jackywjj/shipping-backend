"""
Customer controller
"""
from fastapi import APIRouter
from starlette.requests import Request

from app.utils.factory import ResponseFactory
from app.schemas.customer_schema import CustomerForm
from app.services.customer_service import CustomerService
from app.utils.response_json import response_success

router = APIRouter(prefix="/api/customers", tags=['客户模块'])


@router.post("")
async def create_customer(customer_form: CustomerForm):
    err = CustomerService.create_customer(customer_form)
    if err is not None:
        return dict(code=110, msg=err)
    return response_success(None)


@router.get("/current")
async def list_customers(request: Request):
    customer_id = request.state.customer_id
    customer = CustomerService.get_customer_by_id(customer_id)
    return response_success(ResponseFactory.model_to_list(customer, 'deleted_at'))


@router.get("")
async def get_customers(request: Request, page_number: int = 1, page_size: int = 10):
    result, err = CustomerService.get_customers(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/all")
async def get_customers():
    result, err = CustomerService.get_all_customers()
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)
