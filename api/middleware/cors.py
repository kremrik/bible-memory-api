from api.config import cfg

from fastapi.middleware.cors import CORSMiddleware


__all__ = ["CORS"]


CORS = {
    "middleware_class": CORSMiddleware,
    "allow_origins": cfg.env.config.cors_origins,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
