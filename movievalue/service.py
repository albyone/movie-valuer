#from movievalue.providers.dummy import DummyProvider
#from movievalue.providers.omdb import OMDbProvider
from movievalue.clients.ebay import EbayClient
from statistics import mean


class MovieValueService:

    def __init__(self):
       self.provider = EbayClient()
#        self.provider = OMDbProvider()

    def value(self, movie):

        if movie.barcode:
            listings = self.provider.search(movie.barcode)
        else:
            listings = self.provider.search(movie.title)

        if not listings:
            return MovieValue(
                value=None,
                confidence="None",
                source="eBay",
                notes="No matching listings",
            )

        prices = [listing["price"] for listing in listings]

        value = round(mean(prices), 2)

        return MovieValue(
            value=value,
            confidence="High",
            source="eBay",
            notes=f"{len(prices)} listings",
        )