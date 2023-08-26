from pydantic import BaseModel


class JWT(BaseModel):
    sub: str
    user_id: str
    admin: bool
    exp: int
