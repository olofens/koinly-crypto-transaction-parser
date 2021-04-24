import requests
import pprint
import json
pp = pprint.PrettyPrinter(indent=2)

# place the header object here
headers = {}

# how many pages are there in your transaction history? (look at koinly)
tot_pages = 0


def getTransactions(page):

    params = (
        ('per_page', '10'),
        ('order', 'date'),
        ('page', str(page)),
    )
    response = requests.get('https://api.koinly.io/api/transactions', headers=headers, params=params)
    print("Page ", page, " ", response)
    return response.json()["transactions"]


all_transactions = []


for i in range(tot_pages):
    all_transactions = all_transactions + getTransactions(i+1)
    print(len(all_transactions))

data = {
    'transactions': all_transactions
}

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

print("done")
