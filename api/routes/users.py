from starlette.status import HTTP_409_CONFLICT
from api.routes.dependencies import (
    paginate_params,
    validate_admin_user,
    validate_user,
)
from api.db.models.users import Users
from schemas.jwt import JWT
from schemas.response.users import User as UserResponse
from schemas.request.users import User as UserRequest

from asyncpg.exceptions import UniqueViolationError  # type: ignore
from fastapi import APIRouter, Depends, HTTPException, status

from typing import List
from uuid import UUID


__all__ = ["router"]


router = APIRouter()
tags = ["users"]


@router.get(
    "/users",
    response_model=List[UserResponse],
    tags=tags,
    dependencies=[Depends(validate_admin_user)],
)
async def get_users(
    pagination: dict = Depends(paginate_params),
):
    limit = pagination["limit"]
    offset = pagination["offset"]

    users = (
        await Users.select()
        .order_by(Users.user_id)
        .limit(limit)
        .offset(offset)
        .run()
    )

    return users


@router.post("/users", response_model=UserResponse, tags=tags)
async def create_user(user: UserRequest):
    try:
        await Users.insert(Users(**user.dict())).run()
        created_user = await Users.select().where(
            Users.username == user.username
        )
        return created_user[0]
    except UniqueViolationError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )


@router.delete(
    "/users/{user_id}",
    response_model=str,
    tags=tags,
    dependencies=[Depends(validate_admin_user)],
)
async def delete_user(user_id: str):
    user_id_u = UUID(user_id)
    try:
        await Users.delete().where(Users.user_id == user_id_u).run()
        return user_id
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.get("/me", response_model=UserResponse, tags=tags)
async def read_users_me(user: JWT = Depends(validate_user)):
    user_id = UUID(user.user_id)
    users = (
        await Users.select().where(Users.user_id == user_id).run()
    )
    return UserResponse(**users[0])


@router.delete("/me", response_model=UserResponse, tags=tags)
async def delete_users_me(user: JWT = Depends(validate_user)):
    user_id = UUID(user.user_id)
    await Users.update({Users.disabled: True}).where(
        Users.user_id == user_id
    ).run()

    users = (
        await Users.select().where(Users.user_id == user_id).run()
    )

    return UserResponse(**users[0])
