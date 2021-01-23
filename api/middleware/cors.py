from fastapi.middleware.cors import CORSMiddleware


__all__ = ["CORS"]


origins = [
    "http://localhost:8081",
]

CORS = {
    "middleware_class": CORSMiddleware,
    "allow_origins": origins,
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}
