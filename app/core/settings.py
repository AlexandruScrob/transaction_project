from functools import lru_cache
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    ###
    # Authentication Credentials
    ###
    auth_username: str
    auth_password: SecretStr

    ###
    # DataBase Settings
    ###
    db_path: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
