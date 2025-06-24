from sqlalchemy import or_

from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.ship import Ship
from app.schemas.ship_schema import ShipForm, UpdateShipForm
from app.utils.logger import logger


class ShipService(object):
    @staticmethod
    def create_ship(ship_form: ShipForm):
        try:
            with Session() as session:
                ships = session.query(Ship).filter(or_(Ship.ship_name == ship_form.ship_name)).all()
                if ships:
                    raise Exception("船只已存在")
                ship = Ship(ship_form.ship_name, ship_form.ship_type, ship_form.ship_capacity)
                session.add(ship)
                session.commit()
        except Exception as e:
            logger.error(f"船只新增失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_ships(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Ship)
                ships = query.filter_by(active=1).offset(offset).limit(page_size).all()
                total = query.filter_by(active=1).count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': ResponseFactory.model_to_list(ships),
                }
                return res, None
        except Exception as e:
            logger.error(f"获取船只列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_all_ships():
        try:
            with Session() as session:
                ships = session.query(Ship).filter_by(active=1).all()
                return ships, None
        except Exception as e:
            logger.error(f"获取船只列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_ship_by_id(ship_id):
        try:
            with Session() as session:
                ship = session.query(Ship).filter_by(id=ship_id, active=1).one()
                return ship
        except Exception as e:
            logger.error(f"获取船只失败: {str(e)}")
            return None, str(e)

    @staticmethod
    def delete_ship_by_id(ship_id):
        try:
            with Session() as session:
                ship = session.query(Ship).filter_by(id=ship_id).one()
                ship.active = 0
                session.commit()
        except Exception as e:
            logger.error(f"删除船只失败: {str(e)}")

    @staticmethod
    def update_ship_info(update_ship_form: UpdateShipForm):
        try:
            with Session() as session:
                ship = session.query(Ship).filter_by(id=update_ship_form.ship_id).one()
                if ship is None:
                    raise Exception("船只不存在")
                ship.ship_name = update_ship_form.ship_name
                ship.ship_type = update_ship_form.ship_type
                ship.ship_capacity = update_ship_form.ship_capacity
                ship.status = update_ship_form.status
                session.commit()
        except Exception as e:
            logger.error(f"修改船只信息失败: {str(e)}")
            return str(e)
        return None
