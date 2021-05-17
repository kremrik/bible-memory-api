from pydantic import BaseModel

from typing import List


__all__ = ["EnvCfg", "environments"]


class EnvCfg(BaseModel):
    cors_origins: List[str]


environments = {
    "local": EnvCfg(cors_origins=["http://localhost:8081"])
}
