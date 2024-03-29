from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Boolean
from piccolo.columns.column_types import Text
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import UUID
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampNow
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod


ID = "2021-05-31T15:29:38"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="bible_memory"
    )

    manager.add_table("Users", tablename="users")

    manager.add_table("Passages", tablename="passages")

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
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
        },
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
            "unique": True,
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
            "unique": True,
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

    manager.add_column(
        table_class_name="Users",
        tablename="users",
        column_name="user_id",
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

    manager.add_column(
        table_class_name="Passages",
        tablename="passages",
        column_name="user_id",
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

    manager.add_column(
        table_class_name="Passages",
        tablename="passages",
        column_name="passage",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary": False,
            "key": False,
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
        },
    )

    return manager
