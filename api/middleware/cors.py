from api.config import cfg

from fastapi.middleware.cors import CORSMiddleware


__all__ = ["CORS"]


CORS = {
    "middleware_class": CORSMiddleware,
    "allow_origin_regex": cfg.middleware.cors_regex,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
