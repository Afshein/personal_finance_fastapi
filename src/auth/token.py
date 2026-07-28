from __future__ import annotations

from uuid import uuid4

from settings import config

import redis

r = redis.Redis(
    host=config.redis_host,
    port=6379,
    db=0,
    decode_responses=True,
)


def store_token(
    connection_id: bytes | str,
    token: str,
) -> None:
    r.set(connection_id, token)


def load_token(connection_id: str) -> bytes | str | None:
    return r.get(connection_id)


def generate_connection_id() -> str:
    return str(uuid4())
