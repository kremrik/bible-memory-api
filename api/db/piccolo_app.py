from piccolo.conf.apps import AppConfig
from api.db.models.users import Users

from os.path import abspath, dirname, join


PWD = dirname(abspath(__file__))


APP_CONFIG = AppConfig(
    app_name="bible_memory",
    migrations_folder_path=join(PWD, "migrations"),
    table_classes=[Users],
)
