import requests

Url = ' http://127.0.0.1:8000/stuinfo/1'

r = requests.get(url = Url)

response = r.json()

print(response)