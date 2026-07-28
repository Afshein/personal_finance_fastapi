from __future__ import annotations

from fastapi import FastAPI
from routers.auth import auth_router
from routers.data import data_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(data_router)
