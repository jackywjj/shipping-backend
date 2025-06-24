from sqlalchemy import and_

from app.models import Session
from app.models.port import Port
from app.models.route import Route
from app.schemas.route_schema import RouteForm, UpdateRouteForm, RouteVo
from app.utils.logger import logger


class RouteService(object):
    @staticmethod
    def create_route(route_form: RouteForm):
        try:
            with Session() as session:
                routes = session.query(Route).filter(and_(Route.origin_port_id == route_form.origin_port_id,
                                                          Route.destination_port_id == route_form.destination_port_id)).all()
                if routes:
                    raise Exception("航线已存在")
                route = Route(route_form.origin_port_id, route_form.destination_port_id, route_form.estimated_days)
                session.add(route)
                session.commit()
        except Exception as e:
            logger.error(f"航线新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_routes(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Route)
                routes = query.offset(offset).limit(page_size).all()
                route_vo_list = []
                for route in routes:
                    origin_route = session.query(Port).filter_by(id=route.origin_port_id).one()
                    destination_route = session.query(Port).filter_by(id=route.destination_port_id).one()
                    vo = RouteVo()
                    vo.route_id = route.id
                    vo.origin_port_id = route.origin_port_id
                    vo.origin_port_code = origin_route.port_code
                    vo.origin_port_name = origin_route.port_name
                    vo.destination_port_id = route.destination_port_id
                    vo.destination_port_code = destination_route.port_code
                    vo.destination_port_name = destination_route.port_name
                    vo.estimated_days = route.estimated_days
                    route_vo_list.append(vo)
                total = query.count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': route_vo_list,
                }
                return res, None
        except Exception as e:
            logger.error(f"获取航线列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_all_routes():
        try:
            with Session() as session:
                routes = session.query(Route).all()
                return routes, None
        except Exception as e:
            logger.error(f"获取航线列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_route_by_id(route_id):
        try:
            with Session() as session:
                route = session.query(Route).filter_by(id=route_id).one()
                return route
        except Exception as e:
            logger.error(f"获取航线失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def delete_route_by_id(route_id):
        try:
            with Session() as session:
                route = session.query(Route).filter_by(id=route_id).one()
                session.delete(route)
                session.commit()
        except Exception as e:
            logger.error(f"删除航线失败: {str(e)}")

    @staticmethod
    def update_route_info(update_route_form: UpdateRouteForm):
        try:
            with Session() as session:
                route = session.query(Route).filter_by(id=update_route_form.route_id).one()
                if route is None:
                    raise Exception("航线不存在")
                route.estimated_days = update_route_form.estimated_days
                session.commit()
        except Exception as e:
            logger.error(f"修改航线信息失败: {str(e)}")
            return str(e)
        return None
