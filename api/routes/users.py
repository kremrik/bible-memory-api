from api.db.operations import (
    select_users,
    insert_user,
    drop_user,
    select_user,
    deactivate_user,
)
from schemas.jwt import JWT
from schemas.response.users import User as UserResponse
from schemas.request.users import User as UserRequest

from api.routes.dependencies import (
    paginate_params,
    validate_admin_user,
    validate_user,
)
from asyncpg.exceptions import UniqueViolationError  # type: ignore
from fastapi import APIRouter, Depends, HTTPException, status

import logging
from typing import List


__all__ = ["router"]


LOGGER = logging.getLogger(__name__)


tags = ["users"]
router = APIRouter(prefix="/users", tags=tags)


@router.get(
    "/",
    response_model=List[UserResponse],
    dependencies=[Depends(validate_admin_user)],
)
async def get_users(
    pagination: dict = Depends(paginate_params),
):
    limit = pagination["limit"]
    offset = pagination["offset"]

    users = await select_users(limit, offset)

    return users


@router.post("/", response_model=UserResponse)
async def create_user(user: UserRequest):
    try:
        await insert_user(user)
        return user
    except UniqueViolationError as e:
        LOGGER.error(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=str(e)
        )


@router.delete(
    "/{user_id}",
    response_model=str,
    dependencies=[Depends(validate_admin_user)],
)
async def delete_user(user_id: str):
    try:
        await drop_user(user_id)
        return user_id
    except Exception as e:
        LOGGER.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.get("/me", response_model=UserResponse)
async def read_users_me(user: JWT = Depends(validate_user)):
    user = await select_user(user.user_id)
    return user


@router.delete("/me", response_model=bool)
async def delete_users_me(user: JWT = Depends(validate_user)):
    try:
        await deactivate_user(user.user_id)
        return True
    except Exception as e:
        LOGGER.error(str(e))
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
