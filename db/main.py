from dotenv import load_dotenv
from pydantic import BaseModel

from os import environ
from typing import Optional


__all__ = ["get_user"]


load_dotenv()
PW_HASH = environ["PW_HASH"]
USER = environ["ALLOWED_USER"]


# TODO: source from schemas
# TODO: add admin field
class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str


def get_user(username: Optional[str]) -> Optional[UserInDB]:
    if username == USER:
        return UserInDB(
            username=username,
            hashed_password=PW_HASH
        )
    return None
