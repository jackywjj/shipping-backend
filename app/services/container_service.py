from app.models import Session
from app.models.container import Container
from app.schemas.container_schema import ContainerForm, UpdateContainerForm
from app.utils.logger import logger


class ContainerService(object):
    @staticmethod
    def create_container(container_form: ContainerForm):
        try:
            with Session() as session:
                container = Container(container_form.origin_port_id, container_form.destination_port_id,
                                      container_form.estimated_days)
                session.add(container)
                session.commit()
        except Exception as e:
            logger.error(f"集装箱新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_containers_by_order(order_id):
        try:
            with Session() as session:
                containers = session.query(Container).filter_by(order_id=order_id).all()
                print(containers)
                return containers
        except Exception as e:
            logger.error(f"获取集装箱列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def delete_container_by_id(container_id):
        try:
            with Session() as session:
                container = session.query(Container).filter_by(id=container_id).one()
                session.delete(container)
                session.commit()
        except Exception as e:
            logger.error(f"删除集装箱失败: {str(e)}")

    @staticmethod
    def update_container_info(update_container_form: UpdateContainerForm):
        try:
            with Session() as session:
                container = session.query(Container).filter_by(id=update_container_form.container_id).one()
                if container is None:
                    raise Exception("集装箱不存在")
                container.estimated_days = update_container_form.estimated_days
                session.commit()
        except Exception as e:
            logger.error(f"修改集装箱信息失败: {str(e)}")
            return str(e)
        return None
