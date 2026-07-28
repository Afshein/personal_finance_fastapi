from __future__ import annotations

import pandas
from auth.token import load_token
from data.data import get_account_balance
from data.data import get_accounts
from fastapi import APIRouter

data_router = APIRouter(prefix="/data")


@data_router.get("/balance")
def get_all_account_balance(
    connection_id: str,
):

    token = load_token(connection_id)

    accounts_df = get_accounts(
        token=token,
    )

    accounts = []

    for account_id in accounts_df["account_id"]:
        accounts.append(
            get_account_balance(
                token=token,
                account_id=account_id,
            ),
        )

    df = pandas.concat(accounts)
    return df.to_json(orient="records")
