# pip install requests

import requests
import json

api = 'https://api.exchangerate-api.com/v4/latest/'

currency = input('from: ')
currency2 = input('to: ')

full_url = api+currency.upper()

request = requests.get(full_url)
data = json.loads(request.text)

print(data['rates'][currency2.upper()])
