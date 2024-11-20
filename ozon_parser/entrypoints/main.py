from ozon_parser.config import config

from fastapi import FastAPI


def create_app():
    app = FastAPI(
        debug=config.app.debug,
        title=config.app.app_name,
    )
    return app
