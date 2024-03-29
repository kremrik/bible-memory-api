from api.config import cfg

from jose import jwt  # type: ignore
from passlib.context import CryptContext  # type: ignore
from passlib.hash import bcrypt  # type: ignore


from datetime import datetime, timedelta
from typing import Optional


__all__ = [
    "authenticate_user",
    "create_access_token",
    "hash_plaintext_password",
]


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_plaintext_password(
    password: str, salt: str = None, rounds: int = None
) -> str:
    del salt, rounds  # unused for now, left in API for future
    return bcrypt.hash(password)


def authenticate_user(password: str, hashed_password: str) -> bool:
    if not verify_password(password, hashed_password):
        return False
    return True


def create_access_token(
    data: dict, expires_delta: Optional[timedelta] = None
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        cfg.auth.jwt_secret_key.get_secret_value(),
        algorithm=cfg.auth.algorithm,
    )
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
