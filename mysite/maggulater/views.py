from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
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
		email_ = json_data['email]
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
	return HttpResponse("In the sigup wala")
	# if request.method == "POST" :
	# 	json_data = request.get_json(force = True)

	# args = {}
	# args.update(csrf(request))
	# args['form'] = UserCreationForm()
	# return render_to_response('login_register/register.html', args	)
