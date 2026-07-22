import random

from movievalue.providers.base import Provider
from movievalue.value import MovieValue


class DummyProvider(Provider):

    def lookup(self, movie):

        return MovieValue(
            value=round(random.uniform(2, 20), 2),
            confidence="Dummy",
            source="Dummy Provider",
            notes="Testing only",
        )