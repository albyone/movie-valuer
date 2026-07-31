import requests
from movie_info import MovieInfo
from movievalue.config import OMDB_API_KEY


class OMDbProvider:

    BASE_URL = "https://www.omdbapi.com/"

    def lookup_title(self, title: str):

        response = requests.get(
            self.BASE_URL,
            params={
                "apikey": OMDB_API_KEY,
                "t": title,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if data.get("Response") == "False":
            return None

        return MovieInfo(
            title=data.get("Title", ""),
            year=int(data["Year"]) if data.get("Year", "").isdigit() else None,
            runtime=int(data["Runtime"].replace(" min", ""))
                if data.get("Runtime", "").endswith(" min")
            else None,
            director=data.get("Director", ""),
            genre=data.get("Genre", ""),
            imdb_id=data.get("imdbID", ""),
)