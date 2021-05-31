from api.db.models.passages import Passages
from api.db.models.users import Users
from schemas.request.users import User as UserRequest

from functools import lru_cache
from typing import Union
from uuid import UUID


__all__ = [
    "select_user",
    "select_user_by_username",
    "select_users",
    "insert_user",
    "drop_user",
    "deactivate_user",
    "select_passages",
    "insert_passage",
    "delete_passage",
]


# users
# -------------------------------------------------------------------
async def select_user(user_id: str):
    user_id_u = user_id_to_uuid(user_id)
    users = (
        await Users.select().where(Users.user_id == user_id_u).run()
    )
    return users[0]


async def select_user_by_username(username: str):
    users = (
        await Users.select().where(Users.username == username).run()
    )
    return users[0]


async def select_users(limit: int = 10, offset: int = 0):
    users = (
        await Users.select()
        .order_by(Users.user_id)
        .limit(limit)
        .offset(offset)
        .run()
    )
    return users


async def insert_user(user: UserRequest):
    await Users.insert(Users(**user.dict())).run()


async def drop_user(user_id: str):
    user_id_u = user_id_to_uuid(user_id)
    await Users.delete().where(Users.user_id == user_id_u).run()


async def deactivate_user(user_id: str):
    user_id_u = user_id_to_uuid(user_id)
    await Users.update({Users.disabled: True}).where(
        Users.user_id == user_id_u
    ).run()


# passages
# -------------------------------------------------------------------
async def select_passages(
    user_id: str, limit: int = 10, offset: int = 0
):
    user_id_u = user_id_to_uuid(user_id)
    passages = (
        await Passages.select()
        .where(Passages.user_id == user_id_u)
        .order_by(Users.user_id)
        .limit(limit)
        .offset(offset)
        .run()
    )
    return passages


async def insert_passage(user_id: str, passage: str):
    user_id_u = user_id_to_uuid(user_id)
    record = {"user_id": user_id_u, "passage": passage}
    await Passages.insert(Passages(**record)).run()  # type: ignore


async def delete_passage(user_id: str, passage: str):
    user_id_u = user_id_to_uuid(user_id)
    await Passages.delete().where(
        (Passages.user_id == user_id_u)
        & (Passages.passage == passage)
    ).run()


# -------------------------------------------------------------------
@lru_cache(maxsize=None)
def user_id_to_uuid(user_id: Union[str, UUID]) -> UUID:
    if isinstance(user_id, UUID):
        return user_id
    return UUID(user_id)
