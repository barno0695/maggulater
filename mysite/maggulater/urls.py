from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signUp/$', views.signUp, name = 'signUp'),
	# url(r'^index/$' , views.home, name = 'Index'),
	url(r'^faculty/$' , views.faculty, name = 'faculty'),
	url(r'^home/$', views.home , name = 'home'),
	url(r'^profile/$', views.profile , name = 'profile'),
	url(r'^listcourses/$', views.listcourses , name = 'listcourses'),
	url(r'^allcourses/$', views.allcourses , name = 'allcourses'),
	url(r'^allfacultycourses/$', views.allfacultycourses , name = 'allfacultycourses'),
	url(r'^allstudentcourses/$', views.allstudentcourses , name = 'allstudentcourses'),
	url(r'^listfacultycourses/$', views.listfacultycourses , name = 'listfacultycourses'),
	url(r'^liststudentcourses/$', views.liststudentcourses , name = 'liststudentcourses'),
	# url(r'^index/$' , views.home, name = 'Index'),

]
