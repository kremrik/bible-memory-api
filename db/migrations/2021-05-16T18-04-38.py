from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Boolean
from piccolo.columns.column_types import Varchar
from piccolo.columns.indexes import IndexMethod


ID = "2021-05-16T18:04:38"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(migration_id=ID, app_name="bible_memory")

    manager.add_table("Users", tablename="users")

    manager.add_column(
        table_class_name="Users",
        tablename="users",
        column_name="username",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
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
        table_class_name="Users",
        tablename="users",
        column_name="email",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
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
        table_class_name="Users",
        tablename="users",
        column_name="full_name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
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
        table_class_name="Users",
        tablename="users",
        column_name="disabled",
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
