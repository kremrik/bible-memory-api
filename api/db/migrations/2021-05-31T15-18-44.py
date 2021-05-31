from piccolo.apps.migrations.auto import MigrationManager
from piccolo.columns.column_types import Text
from piccolo.columns.column_types import UUID
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.uuid import UUID4


ID = "2021-05-31T15:18:44"
VERSION = "0.19.1"


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="bible_memory"
    )

    manager.alter_column(
        table_class_name="Passages",
        tablename="passages",
        column_name="user_id",
        params={"default": UUID4()},
        old_params={"default": ""},
        column_class=UUID,
        old_column_class=Varchar,
    )

    manager.alter_column(
        table_class_name="Passages",
        tablename="passages",
        column_name="passage",
        params={"unique": True, "default": ""},
        old_params={"unique": False, "default": UUID4()},
        column_class=Text,
        old_column_class=UUID,
    )

    return manager
