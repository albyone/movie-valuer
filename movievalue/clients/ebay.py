import requests

from movievalue.config import (
    EBAY_CLIENT_ID,
    EBAY_CLIENT_SECRET,
)


class EbayClient:

    TOKEN_URL = "https://api.ebay.com/identity/v1/oauth2/token"

    def __init__(self):
        self._access_token = None

    def _get_access_token(self):

        response = requests.post(
            self.TOKEN_URL,
            auth=(EBAY_CLIENT_ID, EBAY_CLIENT_SECRET),
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    @property
    def access_token(self):

        if self._access_token is None:
            token = self._get_access_token()
            self._access_token = token["access_token"]

        return self._access_token