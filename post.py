import json
import urllib2
import requests

data = {
        'email' : "shubham@gmail.com",
        'password' : "shubham123"
}
url = 'https://127.0.0.1:5000/login'
# payload = {'some': 'data'}
headers = {'content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)
print response
