from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.message import Message
from app.schemas.message_schema import MessageForm
from app.utils.logger import logger


class MessageService(object):
    @staticmethod
    def create_message(message_form: MessageForm):
        try:
            with Session() as session:
                message = Message(message_form.message_title, message_form.message_content)
                session.add(message)
                session.commit()
        except Exception as e:
            logger.error(f"用户反馈新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_last_messages():
        try:
            with Session() as session:
                messages = session.query(Message).filter_by(active=1).order_by(Message.sent_at.desc()).limit(5).all()
                res = {
                    'data': ResponseFactory.model_to_list(messages),
                }
                return res, None
        except Exception as e:
            logger.error(f"获取用户反馈列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_messages(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Message)
                messages = query.filter_by(active=1).offset(offset).limit(page_size).all()
                total = query.filter_by(active=1).count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': ResponseFactory.model_to_list(messages),
                }
                return res, None
        except Exception as e:
            logger.error(f"获取用户反馈列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_message_by_id(message_id):
        try:
            with Session() as session:
                message = session.query(Message).filter_by(id=message_id, active=1).one()
                return message
        except Exception as e:
            logger.error(f"获取用户反馈失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def delete_message_by_id(message_id):
        try:
            with Session() as session:
                message = session.query(Message).filter_by(id=message_id).one()
                message.active = 0
                session.commit()
        except Exception as e:
            logger.error(f"删除用户反馈失败: {str(e)}")
