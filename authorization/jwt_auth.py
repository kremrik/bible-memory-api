from api.config import cfg
from schemas.jwt import JWT

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
) -> JWT:
    return _validate_token(token)


def _validate_token(token: str) -> JWT:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            cfg.auth.jwt_secret_key.get_secret_value(),
            algorithms=[cfg.auth.algorithm],
        )
        return JWT(**payload)

    except JWTError:
        raise credentials_exception
