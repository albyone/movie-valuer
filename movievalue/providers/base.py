from abc import ABC, abstractmethod

from movievalue.models import Movie
from movievalue.value import MovieValue


class Provider(ABC):

    @abstractmethod
    def lookup(self, movie: Movie) -> MovieValue:
        """Lookup a movie."""
        raise NotImplementedError