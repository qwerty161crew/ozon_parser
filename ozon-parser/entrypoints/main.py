from fastapi import FastAPI

from ozon_parser.config import config
from ozon_parser.routers.v1 import ozon_router

routers = (ozon_router,)


def create_app():
    app = FastAPI(
        debug=config.app.debug,
        title=config.app.app_name,
    )
    for router in routers:
        app.include_router(router)
    return app
