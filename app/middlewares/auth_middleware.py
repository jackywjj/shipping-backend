from fastapi import Request
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from app.components.user_token import UserToken
from app.excpetions.request_exception import AuthException


class AuthMiddleware(BaseHTTPMiddleware):
    """ 用户认证中间件"""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        path: str = request.get('path')
        if (path.startswith('/api/auth/login') | path.startswith('/api/captcha')
                | path.startswith('/docs') | path.startswith('/openapi') | path.startswith('/health')):
            response = await call_next(request)
            return response
        token = request.headers.get("Authorization", "")
        if not token.startswith("Bearer"):
            raise AuthException(status_code=status.HTTP_401_UNAUTHORIZED, detail="用户信息身份认证失败")
        token = token[7:]
        result = UserToken.parse_token(token)
        request.state.user_id = result['user_id']
        result = await call_next(request)
        return result
