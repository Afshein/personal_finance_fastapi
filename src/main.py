from fastapi import FastAPI

app = FastAPI()

from auth.auth import get_auth_url, get_auth_token

@app.get("/")
async def root():
    return get_auth_url()

@app.get("/callback")
async def root(
    code: str,
    scope: str,
):
    return get_auth_token(auth_code = code)
