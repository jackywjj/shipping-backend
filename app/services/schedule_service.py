from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.order import Order
from app.models.route import Route
from app.models.schedule import Schedule
from app.utils.logger import logger


class ScheduleService(object):
    @staticmethod
    def create_schedule(order: Order):
        try:
            with Session() as session:
                route = session.query(Route).filter_by(id=order.route_id).one()
                schedule = Schedule(order.ship_id, order.route_id)
                schedule.departure_time = order.departure_date
                schedule.arrival_time = order.departure_date = route.estimated_days
                session.add(schedule)
                session.commit()
        except Exception as e:
            logger.error(f"航运调度新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_schedules(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Schedule)
                schedules = query.order_by(Schedule.departure_time.asc()).offset(offset).limit(page_size).all()
                total = query.count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': schedules,
                }
                return res, None
        except Exception as e:
            logger.error(f"获取航运调度列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_schedule_by_id(schedule_id):
        try:
            with Session() as session:
                schedule = session.query(Schedule).filter_by(id=schedule_id, active=1).one()
                return schedule
        except Exception as e:
            logger.error(f"获取航运调度失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def update_schedule_by_id(schedule_id, status):
        try:
            with Session() as session:
                schedule = session.query(Schedule).filter_by(id=schedule_id).one()
                schedule.status = status
                session.commit()
        except Exception as e:
            logger.error(f"修改航运调度失败: {str(e)}")
