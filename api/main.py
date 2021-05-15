from api.routes.auth import router as auth  # type: ignore
from api.routes.base import router as base  # type: ignore
from api.routes.passages import router as passages  # type: ignore
from api.routes.users import router as users  # type: ignore
from api.middleware.cors import CORS

from fastapi import FastAPI


__all__ = ["start"]


def start():
    app = FastAPI()

    app.include_router(base)
    app.include_router(passages)
    app.include_router(auth)
    app.include_router(users)

    app.add_middleware(**CORS)  # type: ignore

    return app
