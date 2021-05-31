from api.routes import auth
from api.routes import base
from api.routes import passages
from api.routes import users

from fastapi import FastAPI

import logging


__all__ = ["add_routers"]


LOGGER = logging.getLogger(__name__)
ROUTERS = [auth.router, base.router, passages.router, users.router]


def add_routers(app: FastAPI) -> None:
    LOGGER.info("Adding routers")
    for router in ROUTERS:
        app.include_router(router)
