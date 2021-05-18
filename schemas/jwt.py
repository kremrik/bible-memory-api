from pydantic import BaseModel


class JWT(BaseModel):
    sub: str
    admin: bool
    exp: int
