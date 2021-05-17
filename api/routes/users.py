from api.routes.dependencies import validate_user
from api.db.models.users import Users
from schemas.users import User

from fastapi import Depends, APIRouter


__all__ = ["router"]


router = APIRouter()


@router.get("/me", response_model=User)
async def read_users_me(username: str = Depends(validate_user)):
    users = (
        await Users.select().where(Users.username == username).run()
    )
    user = users[0]
    return User(**user)
