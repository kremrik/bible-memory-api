from api.config import cfg
from api.logger import configure_logging
from api.routes import add_routers
from api.middleware import add_middleware
from api.db.engine import engine

from fastapi import FastAPI

import logging
import logging.config


__all__ = ["start"]


configure_logging()
LOGGER = logging.getLogger(__name__)


def start():
    LOGGER.info(cfg)
    app = FastAPI()

    @app.on_event("startup")
    async def create_db_conn():
        LOGGER.info("Creating database connection pool")
        await engine.start_connection_pool()

    @app.on_event("shutdown")
    async def destroy_db_conn():
        LOGGER.info("Shutting down database connection pool")
        await engine.close_connection_pool()

    add_routers(app)
    add_middleware(app)

    return app
