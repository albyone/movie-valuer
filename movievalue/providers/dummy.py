import random

from movievalue.providers.base import Provider
from movievalue.value import MovieValue
from movievalue.models import Movie


class DummyProvider(Provider):

    def lookup(self, movie: Movie):

        return MovieValue(
            value=float(len(movie.title)),
            confidence="Dummy",
            source="Dummy Provider",
            notes="Testing only",
        )