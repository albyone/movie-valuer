#from movievalue.providers.dummy import DummyProvider
#from movievalue.providers.omdb import OMDbProvider
from movievalue.clients.ebay import EbayClient
from movievalue.value import MovieValue
from statistics import mean

UNOPENED_CONDITION = "Unopened"

class MovieValueService:

    def __init__(self):
       self.provider = EbayClient()
#        self.provider = OMDbProvider()

    def value(self, movie):

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
            else:
                notes = "No Brand New listings found. Estimated using used listings."

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

        return MovieValue(
            value=value,
            confidence="High" if len(prices) >= 5 else "Medium" if len(prices) >= 3 else "Low",
            source="eBay",
            notes=f"{len(prices)} listings",
        )