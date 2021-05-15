from pydantic import BaseModel

from typing import List


class EnvCfg(BaseModel):
    cors_origins: List[str]


environments = {
    "local": EnvCfg(cors_origins=["http://localhost:8081"])
}
