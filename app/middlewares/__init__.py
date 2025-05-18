from fastapi import FastAPI

from .auth_middleware import AuthMiddleware
from .logger_middleware import LoggerMiddleware


def register_middleware_handler(server: FastAPI):
    # 添加耗时请求中间件
    server.add_middleware(AuthMiddleware)
    server.add_middleware(LoggerMiddleware)
