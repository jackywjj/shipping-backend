from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=3600, pool_pre_ping=True)
Session = sessionmaker(engine)
# 创建对象的基类:
Base = declarative_base()
# 创建所有表
Base.metadata.create_all(engine)
