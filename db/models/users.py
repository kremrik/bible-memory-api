from piccolo.table import Table
from piccolo.columns import Boolean, Varchar


class Users(Table):
    username = Varchar(length=100)
    email = Varchar(length=100)
    full_name = Varchar(length=100)
    disabled = Boolean(default=False)
