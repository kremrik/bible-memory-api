from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Varchar


ID = "2021-05-16T20:27:35"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="bible_memory")

    manager.alter_column(
        table_class_name="Users",
        tablename="users",
        column_name="username",
        params={"unique": True},
        old_params={"unique": False},
        column_class=Varchar,
        old_column_class=Varchar,
    )

    manager.alter_column(
        table_class_name="Users",
        tablename="users",
        column_name="email",
        params={"unique": True},
        old_params={"unique": False},
        column_class=Varchar,
        old_column_class=Varchar,
    )

    manager.alter_column(
        table_class_name="Users",
        tablename="users",
        column_name="full_name",
        params={"unique": True},
        old_params={"unique": False},
        column_class=Varchar,
        old_column_class=Varchar,
    )

    return manager
