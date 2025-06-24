"""
auth controller
"""
import base64

from captcha.image import ImageCaptcha
from fastapi import APIRouter
from starlette.requests import Request

from app.components.user_token import UserToken
from app.constants.app_constant import (CACHE_CAPTCHA_PREFIX,
                                        CACHE_CAPTCHA_EXPIRATION)
from app.excpetions.biz_exception import BizError
from app.utils.factory import ResponseFactory
from app.schemas.auth_schema import LoginForm
from app.services.user_service import UserService
from app.utils.helper import render_captcha_value
from app.utils.response_json import response_success

router = APIRouter(prefix="/api", tags=['认证模块'])


@router.get("/captcha", summary='获取验证码')
async def get_captcha(request: Request):
    """
    获取验证码
    """
    image = ImageCaptcha()
    captcha_code = render_captcha_value(6).lower()
    captcha_value = render_captcha_value(4)
    image_data = image.generate(captcha_value)
    captcha_image = base64.b64encode(image_data.getvalue())

    await request.app.state.redis.set(CACHE_CAPTCHA_PREFIX + captcha_code, captcha_value)
    await request.app.state.redis.expire(CACHE_CAPTCHA_PREFIX + captcha_code, CACHE_CAPTCHA_EXPIRATION)
    data = {"captcha_image": captcha_image.decode("utf-8"), "captcha_code": captcha_code}
    return response_success(data)


@router.post("/auth/login", summary='登陆模块')
async def login(request: Request, login_form: LoginForm):
    captcha_value = await request.app.state.redis.get(CACHE_CAPTCHA_PREFIX + login_form.captcha_code)
    if captcha_value is None or captcha_value.lower() != login_form.captcha_value.lower():
        raise BizError('验证码错误')
    user, err = UserService.login(login_form.user_name, login_form.user_password)
    if err is not None:
        raise BizError(err)

    token = UserToken.generate_token(user)
    if token is None:
        raise BizError(err)
    data = {"user_token": token, "user_info": ResponseFactory.model_to_dict(user, 'user_password')}
    return response_success(data)
