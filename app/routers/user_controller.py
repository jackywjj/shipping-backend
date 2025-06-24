from fastapi import APIRouter

from app.excpetions.error_base import ErrorBase
from app.schemas.user_schema import UserForm, UpdateForm
from app.services.user_service import UserService
from app.utils.response_json import response_success, response_error

router = APIRouter(prefix="/api/users", tags=['用户模块'])


@router.post("", summary='新增用户')
async def create_user(user_form: UserForm):
    err = UserService.create_user(user_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="用户创建成功")


@router.get("", summary='分页获取用户列表')
async def get_users(page_number: int = 1, page_size: int = 10):
    result, err = UserService.get_users(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{user_id}", summary='根据用户ID获取用户')
async def get_user_by_id(user_id):
    result = UserService.get_user_by_id(user_id)
    return dict(code=0, msg="", data=result)


@router.put("/update", summary='更新用户')
async def update_user_info(update_form: UpdateForm):
    result = UserService.update_user_info(update_form)
    if result:
        return response_error(ErrorBase(code=500, msg="修改用户信息失败"))
    return response_success()


@router.delete("/{user_id}", summary='删除用户')
async def delete_user(user_id):
    result = UserService.delete_user_by_id(user_id)
    return dict(code=0, msg="", data=result)
