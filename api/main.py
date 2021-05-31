from api.config import cfg
from api.logger import LOG_CFG_FILE_PATH
from api.routes.auth import router as auth
from api.routes.base import router as base
from api.routes.passages import router as passages
from api.routes.users import router as users
from api.middleware.cors import CORS
from api.db.engine import engine

from fastapi import FastAPI

import logging
import logging.config


__all__ = ["start"]


logging.config.fileConfig(
    LOG_CFG_FILE_PATH, disable_existing_loggers=False
)
LOGGER = logging.getLogger(__name__)


def start():
    LOGGER.info(cfg)
    app = FastAPI()

    @app.on_event("startup")
    async def create_db_conn():
        # TODO: log engine configs
        await engine.start_connection_pool()

    @app.on_event("shutdown")
    async def destroy_db_conn():
        await engine.close_connection_pool()

    app.include_router(base)
    app.include_router(passages)
    app.include_router(auth)
    app.include_router(users)

    app.add_middleware(**CORS)  # type: ignore

    return app
