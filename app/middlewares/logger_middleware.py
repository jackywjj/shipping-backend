from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from app import logger


class LoggerMiddleware(BaseHTTPMiddleware):
    """ 日志中间件"""

    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response:
        path: str = request.get("path")
        method = request.method
        query_params = request.query_params
        # 获取请求体
        body = ''
        if method == "POST" or method == "PUT":
            try:
                body = await request.json()
            except Exception as e:
                logger.error(f"Error parsing JSON body: {e}")
                body = {}
        logger.info(f"Request: {method} {path} {query_params} {body}")
        response = await call_next(request)
        print(f"Response: {response.status_code}")
        return response
