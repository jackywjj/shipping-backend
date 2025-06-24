from sqlalchemy import or_

from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.port import Port
from app.schemas.port_schema import PortForm, UpdatePortForm
from app.utils.logger import logger


class PortService(object):
    @staticmethod
    def create_port(port_form: PortForm):
        try:
            with Session() as session:
                ports = session.query(Port).filter(or_(Port.port_code == port_form.port_code)).all()
                if ports:
                    raise Exception("港口已存在")
                port = Port(port_form.port_code, port_form.port_name, port_form.country)
                session.add(port)
                session.commit()
        except Exception as e:
            logger.error(f"港口新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_ports(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Port)
                ports = query.offset(offset).limit(page_size).all()
                total = query.count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': ResponseFactory.model_to_list(ports),
                }
                return res, None
        except Exception as e:
            logger.error(f"获取港口列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_port_by_id(port_id):
        try:
            with Session() as session:
                port = session.query(Port).filter_by(id=port_id).one()
                return port
        except Exception as e:
            logger.error(f"获取港口失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def delete_port_by_id(port_id):
        try:
            with Session() as session:
                port = session.query(Port).filter_by(id=port_id).one()
                port.active = 0
                session.commit()
        except Exception as e:
            logger.error(f"删除港口失败: {str(e)}")

    @staticmethod
    def update_port_info(update_port_form: UpdatePortForm):
        try:
            with Session() as session:
                port = session.query(Port).filter_by(id=update_port_form.port_id).one()
                if port is None:
                    raise Exception("港口不存在")
                port.port_code = update_port_form.port_code
                port.port_name = update_port_form.port_name
                port.country = update_port_form.country
                session.commit()
        except Exception as e:
            logger.error(f"修改港口信息失败: {str(e)}")
            return str(e)
        return None
