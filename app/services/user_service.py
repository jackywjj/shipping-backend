from sqlalchemy import or_

from app.components.user_token import UserToken
from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.user import User
from app.schemas.user_schema import UserForm, UpdateForm
from app.utils.logger import logger


class UserService(object):
    @staticmethod
    def create_user(user_form: UserForm):
        try:
            with Session() as session:
                users = session.query(User).filter(or_(User.user_name == user_form.user_name)).all()
                if users:
                    raise Exception("用户名已存在")
                # 注册的时候给密码加盐
                pwd = UserToken.add_salt(user_form.user_password)
                user = User(user_form.user_name, pwd)
                session.add(user)
                session.commit()
        except Exception as e:
            logger.error(f"用户新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def login(user_name, user_password):
        try:
            pwd = UserToken.add_salt(user_password)
            logger.info(f"Password plain: {pwd}")
            with Session() as session:
                user = session.query(User).filter_by(user_name=user_name, user_password=pwd, active=1).first()
                if user is None:
                    return None, "用户名或密码错误"
                session.commit()
                session.refresh(user)
                return user, None
        except Exception as e:
            logger.error(str(e))
            return None, f"用户{user_name}登录失败"

    @staticmethod
    def get_users(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(User)
                users = query.filter_by(active=1).offset(offset).limit(page_size).all()
                total = query.filter_by(active=1).count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': ResponseFactory.model_to_list(users, 'user_password'),
                }
                return res, None
        except Exception as e:
            logger.error(f"获取用户列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            with Session() as session:
                user = session.query(User).filter_by(id=user_id, active=1).one()
                return user
        except Exception as e:
            logger.error(f"获取用户失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def delete_user_by_id(user_id):
        try:
            with Session() as session:
                user = session.query(User).filter_by(id=user_id, active=1).one()
                user.active = 0
                session.commit()
        except Exception as e:
            logger.error(f"删除用户失败: {str(e)}")

    @staticmethod
    def update_user_info(update_form: UpdateForm):
        try:
            with Session() as session:
                user = session.query(User).filter_by(id=update_form.user_id, active=1).one()
                if user is None:
                    raise Exception("用户不存在")
                # 修改的时候给密码加盐
                if update_form.user_password:
                    pwd = UserToken.add_salt(update_form.user_password)
                    user.user_password = pwd
                if update_form.real_name:
                    user.real_name = update_form.real_name
                if update_form.user_name:
                    user.user_name = update_form.user_name
                session.commit()
        except Exception as e:
            logger.error(f"修改用户信息失败: {str(e)}")
            return str(e)
        return None
