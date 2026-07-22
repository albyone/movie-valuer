from movievalue.providers.dummy import DummyProvider


class MovieValueService:

    def __init__(self):

        self.provider = DummyProvider()

    def value_movie(self, movie):

        return self.provider.lookup(movie)