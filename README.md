# 项目说明

航运订单管理系统

# 系统架构

fastapi+mysql+sqlalchemy+jwt的开发模板

# 目录说明

app/ : 项目的主目录，包含所有应用相关代码。

main.py: 项目的入口文件，启动FastAPI应用。

app/routers/ : 核心功能，如配置、安全等。

app/models/ : 数据库模型

app/schemas/ : 数据模型，用于请求和响应的验证

app/services/ : 服务层，业务逻辑代码

app/utils/ : 工具函数和公用模块

app/components/ : 相关组件，用户Token

app/constants/ : 常量、枚举等

app/exceptions/ : 异常定义

app/handler/ : 异常定义

# 配置相关

.env: 环境变量文件，用于存储敏感信息，如数据库连接字符串。

requirements.txt: 项目依赖列表。

README.md: 项目说明文件。

# 运行项目

cd 到项目根目录下，创建虚拟环境：
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate

## 项目运行
uvicorn main:app --host="127.0.0.1" --port="9090" --reload
