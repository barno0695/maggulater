from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signUp/$', views.signUp, name = 'signUp'),
	url(r'^forgotPassword/$' , views.forgotPassword, name = 'forgotPassword'),
	url(r'^faculty/$' , views.faculty, name = 'faculty'),
	url(r'^home/$', views.home , name = 'home'),
	url(r'^profile/$', views.profile , name = 'profile'),
	url(r'^addLecture/$', views.addLecture, name = 'addLecture'),
	url(r'^listcourses/$', views.listcourses , name = 'listcourses'),
	url(r'^index2/$', views.index2 , name = 'index2'),
	url(r'^allcourses/$', views.allcourses , name = 'allcourses'),
	url(r'^allfacultycourses/$', views.allfacultycourses , name = 'allfacultycourses'),
	url(r'^allstudentcourses/$', views.allstudentcourses , name = 'allstudentcourses'),
	url(r'^listfacultycourses/$', views.listfacultycourses , name = 'listfacultycourses'),
	url(r'^liststudentcourses/$', views.liststudentcourses , name = 'liststudentcourses'),
	url(r'^logout/$', views.logout , name = 'logout'),
	url(r'^enroll/$', views.enroll , name = 'enroll'),
	url(r'^coursehome/(?P<course_id>[0-9]+)/$', views.coursehome , name = 'coursehome'),
	url(r'^coursedetails/$', views.coursedetails , name = 'coursedetails'),

	# url(r'^index/$' , views.home, name = 'Index'),
	url(r'^allnotices/$', views.allnotices , name = 'allnotices'),
	url(r'^allcoursenotices/$', views.allcoursenotices , name = 'allcoursenotices'),
	url(r'^allstudentnotices/$', views.allstudentnotices , name = 'allstudentnotices'),
	url(r'^alllectures/$', views.alllectures , name = 'alllectures'),
	url(r'^allcourselectures/$', views.allcourselectures , name = 'allcourselectures'),
	url(r'^allstudentlectures/$', views.allstudentlectures , name = 'allstudentlectures'),
	url(r'^userdetails/$', views.userdetails , name = 'userdetails'),


]
