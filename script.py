import urllib2,json

url = "http://localhost:5000/addcourse"
postdata = {'c_id': '1000', 'course_name' : 'Makhanewala course ', 	'prereq' : 1, 'faculty_id' : 3}
req = urllib2.Request(url)
req.add_header('Content-Type','application/json')
data = json.dumps(postdata)

response = urllib2.urlopen(req,data)
print response


# url = "http://localhost:5000/login"
# postdata = {'email' : 'shubham@gmail.com' , 'password' : 'shubham123'}
# req = urllib2.Request(url)
# req.add_header('Content-Type','application/json')
# data = json.dumps(postdata)

# response = urllib2.urlopen(req,data)
# print response


# url = "http://localhost:5000/allcourses"
# data = (urllib2.urlopen(url))

# print data


