import requests
import json

Url = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name':'Rahul',
    'roll':101,
    'city':'Ltr'
}
# this data is in python now we have to convert it to json

# dumps to convert python to json
json_data = json.dumps(data)

# post request because we have to send data
response = requests.post(url = Url, data = json_data)

data = response.json()

print(data)
# now we take this json data to url and deserialize it to convert it to complex data