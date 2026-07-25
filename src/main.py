from __future__ import annotations

from auth.auth import get_auth_token
from auth.auth import get_auth_url
from data.data import get_account_balance
from data.data import get_accounts
from fastapi import FastAPI
from settings import Settings

app = FastAPI()

settings = Settings()

settings.truelayer_url = "https://api.truelayer.com"


@app.get("/")
async def root():
    return get_auth_url(
        client_id=settings.client_id,
        redirect_uri=settings.redirect_uri,
        truelayer_auth_url=settings.truelayer_auth_url,
    )


@app.get("/callback")
async def connect(
    code: str,
    scope: str,
):
    resp = get_auth_token(
        client_id=settings.client_id,
        auth_code=code,
        client_secret=settings.client_secret,
        redirect_uri=settings.redirect_uri,
        auth_url=settings.truelayer_auth_url,
    )

    auth_token = resp["access_token"]

    accounts = get_accounts(
        token=auth_token,
    )

    for account_id in accounts["account_id"]:
        get_account_balance(
            token=auth_token,
            account_id=account_id,
        )
