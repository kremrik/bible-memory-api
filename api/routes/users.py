from api.routes.dependencies import active_user
from schemas.users import User

from fastapi import Depends, APIRouter


__all__ = ["router"]


router = APIRouter()


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: User = Depends(active_user),
):
    return current_user
