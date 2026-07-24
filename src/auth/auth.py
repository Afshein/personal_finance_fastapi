from __future__ import annotations

import json
import os
from urllib.parse import urlencode

import requests

TRUELAYER_URL = os.environ["TRUELAYER_URL"]
TRUELAYER_AUTH_URL = os.environ["TRUELAYER_AUTH_URL"]
CLIENT_ID = os.environ["CLIENT_ID"]
REDIRECT_URI = os.environ["REDIRECT_URI"]
CLIENT_SECRET = None

with open("secrets.json") as f:
    secrets = json.load(f)
    CLIENT_SECRET = secrets["client_secret_prod"]

print(REDIRECT_URI)


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
    auth_code: str,
) -> dict:

    auth_token_params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": auth_code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    resp = requests.post(
        url=f"{TRUELAYER_URL}/connect/token",
        data=auth_token_params,
    )

    return resp.json()
