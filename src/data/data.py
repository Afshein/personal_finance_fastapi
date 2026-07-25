from __future__ import annotations

import pandas
import requests
from flatten_json import flatten
from loguru import logger
from requests import Response
from settings import config

config.truelayer_url = "https://api.truelayer.com"


def get_account_data(
    url: str,
    token: str,
) -> Response:
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {token}",
    }
    resp = requests.get(
        url=url,
        headers=headers,
    )

    if resp.status_code != 200:
        logger.error(resp.json())
        raise Exception

    return resp


def get_account_balance(
    token: str,
    account_id: str,
):
    resp = get_account_data(
        url=f"{config.truelayer_url}/data/v1/accounts/{account_id}/balance",
        token=token,
    )

    df = resp_to_df(
        resp=resp,
        columns=[
            "currency",
            "available",
            "current",
            "account_number",
            "overdraft",
            "update_timestamp",
        ],
    )

    return df


def get_accounts(token: str) -> pandas.DataFrame:

    resp = get_account_data(
        url=f"{config.truelayer_url}/data/v1/accounts",
        token=token,
    )

    df = resp_to_df(
        resp=resp,
        columns=[
            "account_id",
            "account_type",
            "display_name",
            "account_number_number",
            "account_number_sort_code",
            "provider_provider_id",
        ],
    )

    return df


def resp_to_df(
    resp: Response,
    columns: list[str],
) -> pandas.DataFrame:
    resp_flat = [flatten(result) for result in resp.json()["results"]]

    df = pandas.DataFrame(
        columns=columns,
        data=resp_flat,
    )

    return df
