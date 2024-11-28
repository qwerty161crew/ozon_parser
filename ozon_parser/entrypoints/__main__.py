import uvicorn

from ozon_parser.config import config

print(config.postgresql.db_url)
uvicorn.run(
    app="ozon_parser.entrypoints.main:create_app",
    factory=True,
    host=config.app.host,
    port=config.app.port,
    reload=config.app.reload,
)
