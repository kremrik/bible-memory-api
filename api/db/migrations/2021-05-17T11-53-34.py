from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Boolean
from piccolo.columns.indexes import IndexMethod


ID = "2021-05-17T11:53:34"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="bible_memory"
    )

    manager.add_column(
        table_class_name="Users",
        tablename="users",
        column_name="admin",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
        },
    )

    return manager
