import json
import urllib2
import requests
import httplib
# #
# # data = {
# #         'email' : "shubham@gmail.com",
# #         'password' : "shubham123"
# # }
url = 'https://127.0.0.1:5000/login'
# # # payload = {'some': 'data'}
# # headers = {'content-type': 'application/json'}
# #
# # response = requests.post(url, data=json.dumps(data), headers=headers)
# # print response
#
data = {"email": "shubham@gmail.com", "password":"shubham123"}
# # headers = {"Content-type": "application/json", "Accept": "text/plain"}
# # conn = httplib.HTTPConnection('127.0.0.1:5000')
# # conn.request("POST", "/login", json.dumps(data), headers)
# # # print request
# #
# # import requests
#
def post_some_dict(dict):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(dict), headers=headers)
#
post_some_dict(data)
# import urllib2,json
#
# url = "http://localhost:5000/login"
# postdata = {'email':'barno@barno', 'password':"lol"}
#
# req = urllib2.Request(url)
# req.add_header('Content-Type','application/json')
# data = json.dumps(postdata)
#
# response = urllib2.urlopen(req,data)
# print response

# import urllib2,json
#
# url = "http://localhost:5000/signUp"
# postdata = {'name': 'Barnopriyo Barua', 'email': 'barno0695@gmail.com' ,'password': 'abc', 'flag': '0 '}
# req = urllib2.Request(url)
# req.add_header('Content-Type','application/json')
# data = json.dumps(postdata)
#
# try:
#     response = urllib2.urlopen(req,data)
# except:
#     pass
# print response
