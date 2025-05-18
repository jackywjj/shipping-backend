import os
from pathlib import Path
from urllib import parse

from dotenv import load_dotenv

# 自动搜索 .env 文件
load_dotenv(verbose=True)

# 或者指定 .env 文件位置
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

ROOT = os.path.dirname(os.path.abspath(__file__))

SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = os.getenv("SERVER_PORT")
LOG_PATH = os.getenv("LOG_PATH")

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PWD = os.getenv("MYSQL_PWD")
DBNAME = os.getenv("DBNAME")

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    MYSQL_USER, parse.quote_plus(MYSQL_PWD), MYSQL_HOST, MYSQL_PORT, DBNAME)

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_DB = os.getenv("REDIS_DB")
