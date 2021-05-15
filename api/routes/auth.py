from api.config import cfg
from authentication.auth import (
    authenticate_user,
    create_access_token,
)
from schemas.auth import Token

from fastapi import (
    Depends,
    APIRouter,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta


__all__ = ["router"]


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
        minutes=cfg.auth.access_token_expire_minutes
    )

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
