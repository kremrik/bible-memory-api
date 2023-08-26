from piccolo.table import Table
from piccolo.columns import Boolean, Text, Timestamp, UUID, Varchar


class Users(Table):
    username = Varchar(length=100, unique=True)
    password_hash = Text()
    email = Varchar(length=100, unique=True)
    full_name = Varchar(length=100, unique=True)
    disabled = Boolean(default=False)
    admin = Boolean(default=False)
    user_id = UUID()
    create_ts = Timestamp()
