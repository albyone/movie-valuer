import requests

from movievalue.config import (
    EBAY_CLIENT_ID,
    EBAY_CLIENT_SECRET,
)

ALLOWED_CONDITIONS = {
    "BRAND NEW",
    "LIKE NEW",
    "VERY GOOD",
}

EXCLUDED_TITLE_TEXT = {
    "SLIPCOVER",
    "CASE ONLY",
    "NO DISC",
    "EMPTY CASE",
    "DIGITAL CODE",
    "ARTWORK ONLY",
}

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

    def search(self, query: str, limit: int = 10):

        response = requests.get(
            "https://api.ebay.com/buy/browse/v1/item_summary/search",
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "X-EBAY-C-MARKETPLACE-ID": "EBAY_AU",
            },
            params={
                "q": query,
                "limit": limit,
            },
            timeout=30,
        )

        response.raise_for_status()

        data = response.json()

        accepted = []

        for item in data.get("itemSummaries", []):

            condition = item.get("condition", "").upper()

            if condition not in ALLOWED_CONDITIONS:
                continue

            title = item["title"].upper()

            if any(text in title for text in EXCLUDED_TITLE_TEXT):
                continue

            shipping_cost = None
            shipping_options = item.get("shippingOptions", [])
            if shipping_options:
                first_option = shipping_options[0]
                shipping_cost = float(first_option.get("shippingCost", {}).get("value", 0))

            accepted.append(
                {
                    "title": item["title"],
                    "condition": item["condition"],
                    "price": float(item["price"]["value"]),
                    "shipping": shipping_cost
                }
            )

            if len(accepted) == 5:
                break

        return accepted