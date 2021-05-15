from api.middleware.auth import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
)
from schemas.auth import Token, User

from dotenv import load_dotenv
from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta
from os import environ


__all__ = ["router"]


load_dotenv()
SECRET_KEY = environ["SECRET_KEY"]
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: User = Depends(get_current_active_user),
):
    return current_user
