from pprint import pprint

from movievalue.providers.omdb import OMDbProvider

provider = OMDbProvider()

movie = provider.lookup_title("Jaws")

pprint(movie)