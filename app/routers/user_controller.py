from fastapi import APIRouter
from starlette.requests import Request

from app.excpetions.error_base import ErrorBase
from app.schemas.user_schema import UserForm, UpdateForm
from app.services.user_service import UserService
from app.utils.response_json import response_success, response_error

router = APIRouter(prefix="/api/users", tags=['用户模块'])


@router.post("")
async def create_user(user_form: UserForm):
    err = UserService.create_user(user_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="用户创建成功")


@router.get("")
async def get_users(request: Request, page_number: int = 1, page_size: int = 10):
    user_id = request.state.user_id

    result, err = UserService.get_users(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{user_id}")
async def get_user_by_id(request: Request, user_id):
    result = UserService.get_user_by_id(user_id)
    return dict(code=0, msg="", data=result)


@router.put("/update")
async def update_user_info(request: Request, update_form: UpdateForm):
    if request.state.user_id != update_form.user_id:
        return response_error(ErrorBase(code=500, msg="用户ID不匹配"))
    result = UserService.update_user_info(update_form)
    if result:
        return response_error(ErrorBase(code=500, msg="修改用户信息失败"))
    return response_success()


@router.delete("/{user_id}")
async def delete_user(request: Request, user_id):
    result = UserService.delete_user_by_id(user_id)
    return dict(code=0, msg="", data=result)
