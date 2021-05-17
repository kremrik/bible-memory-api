from api.config import cfg
from db.main import get_user
from schemas.auth import TokenData

from fastapi import (
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt  # type: ignore


__all__ = ["validate_token"]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def validate_token(
    token: str = Depends(oauth2_scheme),
) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            cfg.auth.secret_key.get_secret_value(),
            algorithms=[cfg.auth.algorithm],
        )
        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

        return username

    except JWTError:
        raise credentials_exception
