#we can use any application java, android to get data from that api we created

import requests

URL = "http://127.0.0.1:8000/stuinfo/2"

r = requests.get(url = URL)

data = r.json()

print(data)