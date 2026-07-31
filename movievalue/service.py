#from movievalue.providers.dummy import DummyProvider
#from movievalue.providers.omdb import OMDbProvider
from movievalue.clients.ebay import EbayClient
from movievalue.value import MovieValue
from statistics import mean

UNOPENED_CONDITION = "Unopened"
OPENED_CONDITION = "nan"

class MovieValueService:

    def __init__(self):
       self.provider = EbayClient()
#        self.provider = OMDbProvider()

    def value(self, movie):

        notes = ""

        if movie.barcode:
            listings = self.provider.search(movie.barcode)
        else:
            listings = self.provider.search(movie.title)

        if movie.condition == UNOPENED_CONDITION:

            brand_new = [
                listing
                for listing in listings
                    if listing["condition"] == "BRAND NEW"
            ]

            if brand_new:
                listings = brand_new
                notes = "No Brand New listings found. Estimated using used listings."

        if movie.condition != UNOPENED_CONDITION:

            not_brand_new = [
                listing
                for listing in listings
                    if listing["condition"] != "BRAND NEW"
            ]

            if not_brand_new:
                listings = not_brand_new
                notes = "Brand New listings removed. Estimated using used listings."


        if not listings:
            return MovieValue(
                value=None,
                confidence="None",
                source="eBay",
                notes="No matching listings",
            )

        prices = [
            listing["price"] + (listing["shipping"] or 0)
            for listing in listings
        ]

        value = round(mean(prices), 2)

        if notes:
            notes += f" ({len(prices)} listing)" if len(prices) == 1 else f" ({len(prices)} listings)"
        else:
            notes = f"{len(prices)} listing" if len(prices) == 1 else f"{len(prices)} listings"

        return MovieValue(
            value=value,
            confidence="High" if len(prices) >= 5 else "Medium" if len(prices) >= 3 else "Low",
            source="eBay",
            notes=notes,
        )