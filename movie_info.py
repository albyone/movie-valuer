from dataclasses import dataclass


@dataclass(slots=True)
class MovieInfo:
    title: str
    year: int | None
    runtime: int | None
    director: str
    genre: str
    imdb_id: str