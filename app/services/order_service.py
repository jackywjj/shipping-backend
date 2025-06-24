from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.order import Order, OrderItem
from app.schemas.order_schema import OrderForm
from app.utils.logger import logger


class OrderService(object):
    @staticmethod
    def create_order(order_form: OrderForm):
        try:
            with Session() as session:
                order = Order(order_form.customer_id, order_form.route_id, order_form.ship_id,
                              order_form.departure_date)
                session.add(order)
                session.commit()
        except Exception as e:
            logger.error(f"订单新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_orders(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Order)
                orders = query.offset(offset).limit(page_size).all()
                total = query.count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': orders,
                }
                return res, None
        except Exception as e:
            logger.error(f"获取订单列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_order_item_list(order_id):
        try:
            with Session() as session:
                order_item_list = session.query(OrderItem).filter_by(order_id=order_id).all()
                return ResponseFactory.model_to_list(order_item_list)
        except Exception as e:
            logger.error(f"获取订单明细失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def get_order_by_id(order_id):
        try:
            with Session() as session:
                order = session.query(Order).filter_by(id=order_id).one()
                return order
        except Exception as e:
            logger.error(f"获取订单失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def update_order_by_id(order_id, order_status):
        try:
            with Session() as session:
                order = session.query(Order).filter_by(id=order_id).one()
                order.order_status = order_status
                session.commit()
        except Exception as e:
            logger.error(f"删除订单失败: {str(e)}")

    @staticmethod
    def get_order_amount():
        try:
            with Session() as session:
                return session.query(Order).count()
        except Exception as e:
            logger.error(f"获取订单失败: {str(e)}")
            return None, str(e)
