from pydantic import BaseModel, validator

from typing import Any, Optional


UUID = Any


class User(BaseModel):
    username: str
    email: Optional[str]
    full_name: Optional[str]
    disabled: Optional[bool] = False
    admin: Optional[bool] = False
    user_id: UUID

    @validator("user_id")
    def convert_user_id(cls, uid):
        return str(uid)
