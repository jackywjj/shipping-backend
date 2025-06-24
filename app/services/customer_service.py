from sqlalchemy import or_

from app.utils.factory import ResponseFactory
from app.models import Session
from app.models.customer import Customer
from app.schemas.customer_schema import CustomerForm
from app.utils.logger import logger


class CustomerService(object):
    @staticmethod
    def create_customer(customer_form: CustomerForm):
        try:
            with Session() as session:
                customers = session.query(Customer).filter(
                    or_(Customer.company_name == customer_form.company_name)).all()
                if customers:
                    raise Exception("客户名已存在")
                customer = Customer(customer_form.company_name, customer_form.contact_name, customer_form.company_phone,
                                    customer_form.company_email, customer_form.company_address)
                session.add(customer)
                session.commit()
        except Exception as e:
            logger.error(f"用户客户失败: {str(e)}")
            return str(e)
        return None

    @staticmethod
    def get_all_customers():
        try:
            with Session() as session:
                customers = session.query(Customer).filter_by(active=1).all()
                return customers, None
        except Exception as e:
            logger.error(f"获取客户列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_customers(page_number, page_size):
        try:
            with Session() as session:
                offset = (page_number - 1) * page_size
                query = session.query(Customer).filter_by(active=1)
                customers = query.offset(offset).limit(page_size).all()
                total = query.count()
                res = {
                    'page_number': page_number,
                    'page_size': page_size,
                    'total': total,
                    'data': ResponseFactory.model_to_list(customers),
                }
                return res, None
        except Exception as e:
            logger.error(f"获取客户列表失败: {str(e)}")
            return [], str(e)

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            with Session() as session:
                customer = session.query(Customer).filter_by(id=customer_id)
                return customer.one_or_none()
        except Exception as e:
            logger.error(f"获取客户失败: {str(e)}")
            return [], str(e)
