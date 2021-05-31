from api.config.environment import EnvCfg, environments

from dotenv import load_dotenv
from pydantic import BaseSettings, BaseModel, Field, SecretStr

from os import environ


__all__ = ["Config"]


load_dotenv()  # TODO: find a way to do without this


class BaseDotenvSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class EsvApi(BaseDotenvSettings):
    api_key: SecretStr = Field(env="API_KEY")


class Auth(BaseDotenvSettings):
    jwt_secret_key: SecretStr = Field(env="JWT_SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


class DB(BaseDotenvSettings):
    driver: str = "postgresql"
    host: str = Field(env="POSTGRES_HOST", default="0.0.0.0")
    database: str = Field(env="POSTGRES_DB")
    port: str = Field(env="POSTGRES_PORT", default="5432")
    username: str = Field(env="POSTGRES_USER")
    password: SecretStr = Field(env="POSTGRES_PASSWORD")


class Env(BaseDotenvSettings):
    env: str = Field(env="ENVIRONMENT", default="local")
    config: EnvCfg = environments[
        environ.get("ENVIRONMENT", "local")
    ]


class Config(BaseModel):
    auth: Auth = Auth()
    env: Env = Env()
    esv_api: EsvApi = EsvApi()
    db: DB = DB()
