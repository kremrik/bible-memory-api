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


__all__ = ["router"]


router = APIRouter()
tags = ["users"]


@router.get("/me", response_model=UserResponse, tags=tags)
async def read_users_me(user: JWT = Depends(validate_user)):
    username = user.sub
    users = (
        await Users.select().where(Users.username == username).run()
    )
    return UserResponse(**users[0])


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
        .order_by(Users.id)
        .limit(limit)
        .offset(offset)
        .run()
    )

    return users


@router.post("/users", response_model=UserResponse, tags=tags)
async def create_user(user: UserRequest):
    try:
        await Users.insert(Users(**user.dict())).run()
        return user
    except UniqueViolationError as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )
