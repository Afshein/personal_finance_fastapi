from __future__ import annotations

from urllib.parse import urlencode

import requests
from auth.token import generate_connection_id
from auth.token import store_token
from fastapi import APIRouter
from loguru import logger
from settings import config

auth_router = APIRouter(
    prefix="/auth",
)


@auth_router.get("/")
def truelayer_auth_url(
    redirect_uri: str = config.redirect_uri,
    client_id: str = config.client_id,
    truelayer_auth_url: str = config.truelayer_auth_url,
) -> str:
    auth_params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "info accounts balance",
        # "providers": "uk-oauth-all"
        "providers": "uk-cs-mock",
    }

    url = truelayer_auth_url + "?" + urlencode(auth_params)
    return url


auth_token_params = {}


@auth_router.get("/login")
def get_auth_token(
    code: str,
    scope: str,
) -> bytes | str | None:

    auth_token_params = {
        "client_id": config.client_id,
        "client_secret": config.client_secret,
        "code": code,
        "redirect_uri": config.redirect_uri,
        "grant_type": "authorization_code",
    }

    resp = requests.post(
        url=f"{config.truelayer_auth_url}/connect/token",
        data=auth_token_params,
    )

    if resp.status_code != 200:
        logger.error(f"{resp.status_code}: {resp.reason}")
        raise Exception

    token = resp.json()["access_token"]
    connection_id = generate_connection_id()

    store_token(
        connection_id,
        token,
    )

    return connection_id
