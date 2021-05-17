from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Text
from piccolo.columns.indexes import IndexMethod


ID = "2021-05-16T19:47:56"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="bible_memory"
    )

    manager.add_column(
        table_class_name="Users",
        tablename="users",
        column_name="password_hash",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
        },
    )

    return manager
