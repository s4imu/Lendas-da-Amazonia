import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, EmailStr, HttpUrl, PostgresDsn, validator

class Settings(BaseSettings):

    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_CLUSTER: str
    MONGO_DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
