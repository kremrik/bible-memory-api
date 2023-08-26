from api.config import cfg

from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine


__all__ = ["DB", "APP_REGISTRY"]


config = {
    "host": cfg.db.host,
    "database": cfg.db.database,
    "user": cfg.db.username,
    "password": cfg.db.password.get_secret_value(),
}


DB = PostgresEngine(config)
APP_REGISTRY = AppRegistry(apps=["api.db.piccolo_app"])
