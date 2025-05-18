# DevTemplate

fastapi+mysql+sqlalchemy+jwt的开发模板

app/ : 项目的主目录，包含所有应用相关代码。

main.py: 项目的入口文件，启动FastAPI应用。
routers/ : 核心功能，如配置、安全等。
models/ : 数据库模型。
schemas/ : 数据模型，用于请求和响应的验证。
services/ : 数据库操作（CRUD：创建、读取、更新、删除）。
db/ : 数据库相关设置和会话管理。
utils/ : 工具函数和公用模块。

.env: 环境变量文件，用于存储敏感信息，如数据库连接字符串。

alembic/ : 数据库迁移工具Alembic的配置目录。

requirements.txt: 项目依赖列表。

Dockerfile: Docker配置文件，用于容器化部署。

README.md: 项目说明文件。

source venv/bin/activate

uvicorn main:app --host="127.0.0.1" --port="9090" --reload
