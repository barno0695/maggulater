import urllib2,json

url = "http://localhost:5000/signUp"
postdata = {'name': 'Barnopriyo Barua', 'email': 'barno0695@gmail.com' ,'password': 'abc', 'flag': '0'}
req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
print response