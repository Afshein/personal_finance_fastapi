from __future__ import annotations

from auth.auth import get_auth_token
from auth.auth import get_auth_url
from data.conn import create_conn
from fastapi import FastAPI
from settings import Settings

app = FastAPI()

settings = Settings()


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
    resp = get_auth_token(auth_code=code)
    auth_token = resp["access_token"]
    create_conn(auth_token=auth_token)
