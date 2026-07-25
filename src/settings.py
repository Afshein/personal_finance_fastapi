from __future__ import annotations

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    truelayer_url: str = "https://api.truelayer.com"
    truelayer_auth_url: str
    client_id: str
    # client_secret: SecretStr
    client_secret: str
    redirect_uri: str

    model_config = SettingsConfigDict(env_file=".env.prod", env_file_encoding="utf-8")


config = Settings()
