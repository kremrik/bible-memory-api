from piccolo.table import Table
from piccolo.columns import Boolean, Text, Varchar


class Users(Table):
    username = Varchar(length=100, unique=True)
    password_hash = Text()
    email = Varchar(length=100, unique=True)
    full_name = Varchar(length=100, unique=True)
    disabled = Boolean(default=False)
    admin = Boolean(default=False)
