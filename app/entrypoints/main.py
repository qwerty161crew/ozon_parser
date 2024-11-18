from fastapi import FastAPI

from config import config


def create_app():
    app = FastAPI(
        debug=config.app.debug,
        title=config.app.app_name,
    )
    return app
