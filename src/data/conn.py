from __future__ import annotations

import requests

connection_url = "https://api.truelayer.com/v3/data-connections"

conn_params = {
    "scopes": [
        "info",
    ],
    "provider_selection": {
        "type": "preselected",
        "provider_id": "eg-provider",
    },
    "user": {
        "id": "f9b48c9d-176b-46dd-b2da-fe1a2b77350c",
        "name": "Remi Terr",
        "email": "remi.terr@aol.com",
        "phone": "+447777777777",
    },
    "user_consent": {
        "type": "precaptured",
        "captured_at": "2025-01-01T00:00:00.000Z",
    },
    "data_access_type": "recurring",
}


def create_conn(
    auth_token: str,
):
    headers = {
        "Authorization": f"Bearer {auth_token}",
    }

    resp = requests.post(
        url=connection_url,
        headers=headers,
        data=conn_params,
    )

    print(resp.status_code)
    print(resp.json())
