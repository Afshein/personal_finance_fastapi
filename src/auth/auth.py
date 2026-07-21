import requests
from urllib.parse import urlencode
import json

def main():
    print("Hello from personal-finance-fastapi!")

client_id = None
client_secret = None
redirect_uri = None

with open("secrets.json") as f:
    secrets = json.load(f)
    client_id = secrets["client_id"]
    client_secret = secrets["client_secret"]
    redirect_uri = secrets["redirect_uri"]

truelayer_url = "https://auth.truelayer.com"

auth_params = {
    "response_type": "code",
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "scope": "info accounts balance",
    "providers": "uk-oauth-all"
}
def get_auth_url(
    truelayer_url = truelayer_url,
    auth_params = auth_params,
    ):

    url = truelayer_url + "?" + urlencode(auth_params)
    return url

auth_token_params = {}

def get_auth_token(
    truelayer_connect_url = "https://auth.truelayer.com/connect/token",
    auth_code = None,
    ):

    auth_token_params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }

    resp = requests.post(
        url = truelayer_connect_url,
        data = auth_token_params,
    )

    with open('token.json', 'w') as f:
        json.dump(resp.json(), f)
    

    