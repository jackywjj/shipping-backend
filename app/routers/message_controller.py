from fastapi import APIRouter

from app.schemas.message_schema import MessageForm
from app.services.message_service import MessageService

router = APIRouter(prefix="/api/messages", tags=['消息模块'])


@router.post("")
async def create_message(message_form: MessageForm):
    err = MessageService.create_message(message_form)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="消息创建成功")


@router.get("/last")
async def get_last_messages():
    result, err = MessageService.get_last_messages()
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("")
async def get_messages(page_number: int = 1, page_size: int = 10):
    result, err = MessageService.get_messages(page_number, page_size)
    if err is not None:
        return dict(code=110, msg=err)
    return dict(code=0, msg="", data=result)


@router.get("/{message_id}")
async def get_message_by_id(message_id):
    result = MessageService.get_message_by_id(message_id)
    return dict(code=0, msg="", data=result)


@router.delete("/{message_id}")
async def delete_message(message_id):
    result = MessageService.delete_message_by_id(message_id)
    return dict(code=0, msg="", data=result)
