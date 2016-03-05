from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
import json
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from models import *
from django.core.urlresolvers import reverse

# Create your views here.

def home(request):
	print "Here in home "
	return render(request, "maggulater/login.html")

@ensure_csrf_cookie
def login(request):
	print "Here in Login!!!"
	if request.method == 'POST':
		print "yaha aaya !! "
		json_data = request.body
		print request.body
		if not json_data:
			print "hehehehe"
			print("error")
			return redirect('/login/')


			response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		json_data = json.loads(json_data)
		print json_data
		email_ = json_data['email']
		pwd = json_data['password']
		print email_, pwd
		user = MyUser.objects.get(email = email_)
		print "IN LOGIN"
		if user and user.check_password(pwd):
			request.session['id'] = user.user_id
			print request.session
			print "In profile redirect"
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/profile/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			print "IN login wala !! "
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
			return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET':
		print "get h"
		return render(request,'maggulater/login.html')



def faculty(request):
	if request.method == 'GET':
		return render(request, 'maggulater/faculty.html')
def signUp(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		name = json_data['name']
		email = json_data['email']
		link_to_dp = "link"
		type_flag = json_data['flag']
		dob = json_data['dob']
		password = json_data['password']
		user = MyUser(name = name, email = email, link_to_dp = link_to_dp , type_flag = type_flag , dob = dob)
		hashed_pass = user.make_password(password)
		user.set_password(password)
		user.save()
		duser = User.objects.create_user(name,email,password)
		print "Created Users succesfully"
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/login/'}
		return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET':
		return render(request, 'maggulater/signup.html')


def profile(request):
	print "user_id" , request.session['id']
	return render(request, "maggulater/profile.html")


def studenthome(request):
	print "student_id" , request.session['id']
	return render(request , 'maggulater/student.html')


def facultyhome(request):
	print "faculty_id" , request.session['id']
	return render(request , 'maggulater/faculty.html')


def adminhome(request):
	print "admin_id" , request.session['id']
	return render(request , 'maggulater/admin.html')


def parentPortal(request):
	if request.method == 'POST' :
		json_data = request.body
		if not json_data :
			print ("Error !! No credentials Given !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/parentPortal/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		json_data = json.loads(json_data)
		_email = json_data['Email']
		user = MyUser.objects.get(email = email_)
		if user is None or user.email != _email :
			print("Sorry Wrong Credentials !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/parentPortal/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			Performance = Performance_Sheet.objects.get(Student_Id = user.user_id)
			return render(request , 'maggulater/Parent_Portal.html')


def forgotPassword(request):
	if request.method == 'POST' :
		json_data = request.body
		if not json_data :
			print ("Error !! No credentials Given !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/forgotPassword/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		json_data = json.loads(json_data)
		_email = json_data['Email']
		user = User.objects.get(email = _email)
		if user is None or user.email != _email :
			print("Sorry Wrong Credentials !! ")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/forgotPassword/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			password = user.password
			context = {
			'Password' : password
			}
			return context


def logout(request):
	try:
		del request.session['id']
	except KeyError:
		pass
	response = {'status': 1, 'message': "Confirmed!!", 'url':'/home/'}
	return HttpResponse(json.dumps(response), content_type='application/json')


def searchcourse(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/searchcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['course_id']

		course = Course.objects.get(course_id = cid)

		if course:
			request.session['course_id'] = cid
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/searchcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET':
		return render(request , 'maggulater/student_home.html')


# API for enrolling a student in a course
def enroll(request):
	newenroll = Enrolls(student_id = request.session['id'],student_id = request.session['course_id'])
	newenroll.save()
	response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
	return HttpResponse(json.dumps(response), content_type='application/json')


# API to add a new notice
def addnotice(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/addnotice/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['c_id']
		msg = json_data['message']

		newnotice = Notice(timestamp = now(), message = msg, c_id = cid)
		newnotice.save()
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/coursehome/'}
		return HttpResponse(json.dumps(response), content_type='application/json')


# API to add a new course
def addcourse(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/searchcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['c_id']
		cname = json_data['course_name']
		pre = json_data['prereq']
		fac_id = json_data['faculty_id']
		course = Course.objects.get(course_id = cid)

		if course:
			perror("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'/addcourse/'}
			return HttpResponse(json.dumps(response), content_type='application/json')

		newcourse = Course(course_id = cid,course_name = cname,prereq = pre,faculty = fac_id)
		newcourse.save()
		response = {'status': 1, 'message': "Confirmed!!", 'url':'/facultyhome/'}
		return HttpResponse(json.dumps(response), content_type='application/json')


# API to approve a course
def approve(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		if not json_data:
			print("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'approve'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		cid = json_data['c_id']

		course = Course.objects.get(course_id = cid)

		if course:
			course.approve()
			response = {'status': 1, 'message': "Confirmed!!", 'url':'coursehome'}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else:
			perror("error")
			response = {'status': 1, 'message': "Confirmed!!", 'url':'error'}
			return HttpResponse(json.dumps(response), content_type='application/json')


# API to get list of all courses
def allstudentnoticesourses(request):
	j = Course.objects.all()
	d = jsonify(json_data = [i.serialize for i in j])
	return d


# API to get list of all courses of a faculty
def facultycourses(request):
	return jsonify(json_data = [i.serialize for i in Course.objects.get(faculty = request.session['id']).all()])


# API to get all notices
def allnotices(request):
	for i in Notice.objects.all():
		print i.serialize
	return jsonify(json_data = [i.serialize for i in Notice.objects.all()])


# API to get all notices of a course
def allcoursenotices(request):
	return jsonify(json_data = [i.serialize for i in Notice.objects.get(c_id = request.session['course_id']).all()])


# API to get all notices of a student
def allstudentnotices(request):
	enrolled_courses = []
	for c in Enrolls.objects.get(student_id = request.session['id']).all(request):
		p = c.course_id
		enrolled_courses.append(p)

	d = jsonify(json_data = [i.serialize for i in Notice.objects.all() if i.c_id in enrolled_courses])
	return d


# API for listing
def listcourses(request):
	return render(request, 'maggulater/course_list.html')


# API for adding a lecture
def addlecture(request):
	if request.method == 'POST' :
		json_data = result.body
		json_data = json.loads(json_data)
		course_id = request.session['course_id']
		notes = json_data['Notes']
		Date_Time = json_data['Date_Time']
		Topic = json_data['Topic']
		Link = json_data['Link']
		NewLec = Lecture(Course_Id = course_id,Date_Time = Date_Time,Topic =  Topic)
		NewLec.setNotes(notes)
		NewLec.setLink(Link)
		NewLec.save()
		Lecture_Id= NewLec.Lecture_Id
		Questions = json_data['Questions']
		Answers = json_data['Answers']
		NewTest = Test(Lecture_Id = ,Questions = Questions,Answers = Answers)
		NewTest.save()
		response = {'status': 1, 'message': "Confirmed!!", 'url':'coursehome'}
		return HttpResponse(json.dumps(response), content_type='application/json')
