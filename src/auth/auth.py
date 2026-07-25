from __future__ import annotations

from urllib.parse import urlencode

import requests


def get_auth_url(
    redirect_uri: str,
    client_id: str,
    truelayer_auth_url: str,
):
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


def get_auth_token(
    client_id: str,
    auth_code: str,
    client_secret: str,
    redirect_uri: str,
    auth_url: str,
) -> dict:

    auth_token_params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }

    resp = requests.post(
        url=f"{auth_url}/connect/token",
        data=auth_token_params,
    )

    return resp.json()
