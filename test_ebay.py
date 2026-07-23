from pprint import pprint

from movievalue.clients.ebay import EbayClient

client = EbayClient()

token = client.access_token

pprint(token)