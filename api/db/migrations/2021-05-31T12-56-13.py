from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import UUID
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod


ID = "2021-05-31T12:56:13"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="bible_memory"
    )

    manager.add_table("Passages", tablename="passages")

    manager.add_column(
        table_class_name="Passages",
        tablename="passages",
        column_name="user_id",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 36,
            "default": "",
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
        },
    )

    manager.add_column(
        table_class_name="Passages",
        tablename="passages",
        column_name="passage",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary": False,
            "key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
        },
    )

    return manager
