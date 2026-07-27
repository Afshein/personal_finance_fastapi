from __future__ import annotations

import os

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

env_file = os.environ["CONFIG_ENV_FILE"]


class Settings(BaseSettings):
    truelayer_url: str = "https://api.truelayer.com"
    truelayer_auth_url: str
    client_id: str
    # client_secret: SecretStr
    client_secret: str
    redirect_uri: str

    model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8")


config = Settings()
