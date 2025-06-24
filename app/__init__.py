from contextlib import asynccontextmanager

from aioredis import Redis, create_redis_pool
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.excpetions.biz_exception import BizError
from app.utils.logger import logger
from settings import REDIS_HOST, REDIS_PASSWORD, REDIS_DB


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时的代码
    app.state.redis = await create_redis()
    logger.info("init redis success")
    yield
    # 关闭时的代码
    app.state.redis.close()
    await app.state.redis.wait_closed()
    logger.info("Application is shutting down")


async def create_redis() -> Redis:
    return await create_redis_pool("redis://" + REDIS_HOST + "?encoding=utf-8",
                                   #password=REDIS_PASSWORD,
                                   db=int(REDIS_DB))


app = FastAPI(lifespan=lifespan)


def error_map(error_type: str, error_message: str):
    if "missing" in error_type:
        return error_message
    if "params" in error_type:
        return error_message
    if "not_allowed" in error_type:
        return error_message
    if "value_error" in error_type:
        return error_message


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "code": 500,
            "msg": exc,
        })
    )


@app.exception_handler(BizError)
async def unexpected_biz_error(request: Request, exc: BizError):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "code": 500,
            "msg": str(exc),
        })
    )


@app.exception_handler(Exception)
async def unexpected_exception_error(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "code": 500,
            "msg": str(exc),
        })
    )
