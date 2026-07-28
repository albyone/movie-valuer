from pprint import pprint

from movievalue.clients.ebay import EbayClient

client = EbayClient()

prices = client.search("9321337082288")

#print(prices)

for item in prices:
    print(item["title"])
    print(item["condition"])
    print(item["price"])
    print(item["shipping"])
    print()