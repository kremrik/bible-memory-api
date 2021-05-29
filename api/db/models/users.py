from piccolo.table import Table
from piccolo.columns import Boolean, Text, UUID, Varchar


# TODO: add a user_id field as UUID
#  user_id will then need to be passed around instead of username
#  UPDATE: UUID type is not a string, which makes comparisons a pain
class Users(Table):
    username = Varchar(length=100, unique=True)
    password_hash = Text()
    email = Varchar(length=100, unique=True)
    full_name = Varchar(length=100, unique=True)
    disabled = Boolean(default=False)
    admin = Boolean(default=False)
    user_id = UUID()
