from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Timestamp
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.indexes import IndexMethod


ID = "2021-05-31T13:01:04"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="bible_memory"
    )

    manager.add_column(
        table_class_name="Users",
        tablename="users",
        column_name="create_ts",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampNow(),
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
        },
    )

    return manager
