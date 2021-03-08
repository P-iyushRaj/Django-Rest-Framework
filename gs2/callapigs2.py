#getting data from the user and passing it to the api aplication to save it

import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name':'piyush',
    'roll' : 11,
    'city' : 'bhagalpur'
}

json_data = json.dumps(data)

r = requests.post(url = URL, data= json_data)

data = r.json()

print(data)