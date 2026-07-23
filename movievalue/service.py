from movievalue.providers.dummy import DummyProvider
from movievalue.providers.omdb import OMDbProvider


class MovieValueService:

    def __init__(self):
#       self.provider = DummyProvider()
        self.provider = OMDbProvider()

    def value_movie(self, movie):

        return self.provider.lookup(movie)