from __future__ import annotations

from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    truelayer_url: str
    truelayer_auth_url: str
    client_id: str
    client_secret: SecretStr
    redirect_uri: str

    model_config = SettingsConfigDict(env_file=".env.dev", env_file_encoding="utf-8")
