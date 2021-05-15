from authentication.auth import (
    get_current_active_user,
)
from schemas.auth import User

from fastapi import Depends, APIRouter


__all__ = ["router"]


router = APIRouter()


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: User = Depends(get_current_active_user),
):
    return current_user
