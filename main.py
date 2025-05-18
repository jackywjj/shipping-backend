import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute

from app import app, middlewares
from app.routers import auth_controller
from app.routers import customer_controller
from app.routers import dashboard_controller
from app.routers import user_controller
from settings import SERVER_PORT, SERVER_HOST

app.include_router(dashboard_controller.router)
app.include_router(user_controller.router)
app.include_router(auth_controller.router)
app.include_router(customer_controller.router)

middlewares.register_middleware_handler(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Health Checks
_healthChecks = HealthCheckFactory()
app.add_api_route('/health', endpoint=healthCheckRoute(factory=_healthChecks))

if __name__ == "__main__":
    uvicorn.run(app=app, host=SERVER_HOST, port=int(SERVER_PORT))
