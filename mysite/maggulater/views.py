from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User
from models import *
# Create your views here.


def home(request):

	print "Here in chota wala home "
	return render(request, "maggulater/login.html")

def Home(request):
	print "Here in home"
	return HttpResponse("Home sweet Home !!")

@ensure_csrf_cookie
def login(request):
	print "Here in Login!!!"
	if request.method == 'POST':
		print "yaha aaya !! "
		json_data = request.POST
		print request.POST
		if not json_data:
			print("error")
			return redirect('/login/')
		email_ = json_data['email']
		pwd = json_data['password']
		print email_, pwd
		# user = User.objects.all().filter(email = email_)
		# print "IN LOGIN"
		# if user and user.check_password(pwd):
		# 	# session['email'] = email_
		# 	# session['user_id'] = user.user_id
		# 	print "In profile redirect"
		# 	login_user(user)
		# 	return redirect('/Home/')
		# else:
		# 	print "IN login wala !! "
		# 	return redirect('/login')

	if request.method == 'GET':
		print "get h"
		return render(request,'maggulater/login.html')


def signUp(request):
	if request.method == 'POST':
		json_data = request.body
		json_data = json.loads(json_data)
		name = json_data['name']
		email = json_data['email']
		# link_to_dp = json_data['link_to_dp']
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
		return redirect('/login/')
	
	if request.method == 'GET':
		return render(request, 'maggulater/signup.html')
