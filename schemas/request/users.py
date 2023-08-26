from pydantic import BaseModel, validator


class User(BaseModel):
    username: str
    password_hash: str
    email: str
    full_name: str

    @validator("full_name")
    def validate_full_name(cls, name):
        return name.title()
