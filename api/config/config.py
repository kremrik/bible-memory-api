from dotenv import load_dotenv
from pydantic import BaseSettings, BaseModel, Field, SecretStr


__all__ = ["Config"]


load_dotenv()  # load .env if exists


class BaseEnvSettings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# settings for ESV api
# -------------------------------------------------------------------
class EsvApi(BaseEnvSettings):
    api_key: SecretStr = Field(env="API_KEY")


# auth settings
# -------------------------------------------------------------------
class Auth(BaseEnvSettings):
    jwt_secret_key: SecretStr = Field(env="JWT_SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


# database settings
# -------------------------------------------------------------------
class DB(BaseEnvSettings):
    driver: str = "postgresql"
    host: str = Field(env="POSTGRES_HOST", default="0.0.0.0")
    database: str = Field(env="POSTGRES_DB")
    port: str = Field(env="POSTGRES_PORT", default="5432")
    username: str = Field(env="POSTGRES_USER")
    password: SecretStr = Field(env="POSTGRES_PASSWORD")


# middleware settings
# -------------------------------------------------------------------
class ApmMiddleware(BaseEnvSettings):
    service_name: str = Field(env="APM_SERVICE_NAME")
    server_url: str = Field(env="APM_SERVER_URL")


class CorsMiddleware(BaseEnvSettings):
    cors_regex: str = Field(env="CORS_REGEX")


class Middleware(BaseEnvSettings):
    cors: CorsMiddleware = CorsMiddleware()
    apm: ApmMiddleware = ApmMiddleware()


# main config
# -------------------------------------------------------------------
class Config(BaseEnvSettings):
    env: str = Field(env="ENVIRONMENT", default="local")
    auth: Auth = Auth()
    middleware: Middleware = Middleware()
    esv_api: EsvApi = EsvApi()
    db: DB = DB()
