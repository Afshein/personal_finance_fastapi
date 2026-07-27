from __future__ import annotations

import json
from pathlib import Path

TOKEN_FILE = Path("token_store.json")


def save_token(token: str):
    TOKEN_FILE.write_text(json.dumps({"access_token": token}))


def load_token():
    if TOKEN_FILE.exists():
        return json.loads(TOKEN_FILE.read_text())["access_token"]
    return None
