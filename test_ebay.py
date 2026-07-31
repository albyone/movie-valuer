from pprint import pprint

from movievalue.clients.ebay import EbayClient

client = EbayClient()

prices = client.search("810116910885")

#print(prices)

for item in prices:
    print(item["title"])
    print(item["condition"])
    print(item["price"])
 #   print(item["country"])
    print(item["shipping"])
    print()