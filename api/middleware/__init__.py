from api.middleware.cors import CORS

from fastapi import FastAPI

import logging


LOGGER = logging.getLogger(__name__)


__all__ = ["add_middleware"]


def add_middleware(app: FastAPI) -> None:
    LOGGER.info("Adding middleware")
    app.add_middleware(**CORS)  # type: ignore
