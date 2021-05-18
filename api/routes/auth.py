from api.config import cfg
from authorization.basic_auth import (
    authenticate_user,
    create_access_token,
)
from schemas.response.auth import Token
from api.db.models.users import Users

from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm

from base64 import b64decode
from datetime import timedelta


__all__ = ["router"]


router = APIRouter()
tags = ["auth"]


@router.post("/token", response_model=Token, tags=tags)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    username = b64decode(form_data.username.encode()).decode()
    password = b64decode(form_data.password.encode()).decode()

    users = (
        await Users.select().where(Users.username == username).run()
    )
    user = users[0]
    hashed_password = user.get("password_hash")
    admin = user.get("admin")

    valid_user = authenticate_user(password, hashed_password)

    if not valid_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(
        minutes=cfg.auth.access_token_expire_minutes
    )

    access_token = create_access_token(
        data={"sub": username, "admin": admin},
        expires_delta=access_token_expires,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
