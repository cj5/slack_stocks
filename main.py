import json
import requests

apiBaseUrl = 'https://finnhub.io/api/v1/'
token = 'bs2j4mvrh5rc90r5ada0'
symbol = 'WPP'
dataType = 'quote'

r1 = requests.get(f'{apiBaseUrl}{dataType}/?symbol={symbol}&token={token}')
data = json.dumps(r1.json(), sort_keys=True, indent=4)

# print(data)

currentPrice = r1.json()["c"]
print('Current price:', currentPrice)

r2 = requests.post('/', currentPrice)

print(r2.text)
print(r2.status_code, r2.reason)


