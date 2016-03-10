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
	url(r'^addCourse/$',views.addcourse, name = 'addCourse'),
	url(r'^addNotice/$',views.addnotice , name = 'addNotice'),
	# url(r'^[a-z]*/listcourses/$', views.listcourses , name = 'listcourses'),
	url(r'^index2/$', views.index2 , name = 'index2'),
	url(r'^allcourses/$', views.allcourses , name = 'allcourses'),
	url(r'^allfacultycourses/$', views.allfacultycourses , name = 'allfacultycourses'),
	url(r'^allstudentcourses/$', views.allstudentcourses , name = 'allstudentcourses'),
	url(r'^studentlistcourses/$', views.studentlistcourses , name = 'studentlistcourses'),
	url(r'^listfacultycourses/$', views.listfacultycourses , name = 'listfacultycourses'),
	url(r'^liststudentcourses/$', views.liststudentcourses , name = 'liststudentcourses'),
	url(r'^logout/$', views.logout , name = 'logout'),
	url(r'^enroll/$', views.enroll , name = 'enroll'),
	url(r'^coursehome/(?P<course_id>[0-9]+)/$', views.coursehome , name = 'coursehome'),
	# url(r'^lecture/(?P<lecture_id>[0-9]+)/$', views.lecture , name = 'lecture'),
	url(r'^lecture/$', views.lecture , name = 'lecture'),

	url(r'^coursedetails/$', views.coursedetails , name = 'coursedetails'),

	# url(r'^index/$' , views.home, name = 'Index'),
	url(r'^allnotices/$', views.allnotices , name = 'allnotices'),
	url(r'^studentlistcourses/$', views.studentlistcourses , name = 'studentlistcourses'),
	url(r'^facultylistcourses/$', views.facultylistcourses , name = 'facultylistcourses'),
	url(r'^allcoursenotices/$', views.allcoursenotices , name = 'allcoursenotices'),
	url(r'^studenthome/$', views.studenthome , name = 'studenthome'),
	url(r'^alllectures/$', views.alllectures , name = 'alllectures'),
	url(r'^allcourselectures/$', views.allcourselectures , name = 'allcourselectures'),
	# url(r'^allstudentlectures/$', views.allstudentlectures , name = 'allstudentlectures'),
	url(r'^userdetails/$', views.userdetails , name = 'userdetails'),
	url(r'^getStudentLectures/$', views.getStudentLectures , name = 'getStudentLectures'),
	url(r'^getStudentNotices/$', views.getStudentNotices , name = 'getStudentNotices'),
	url(r'^getFacultyLectures/$', views.getFacultyLectures , name = 'getFacultyLectures'),
	url(r'^getFacultyNotices/$', views.getFacultyNotices , name = 'getFacultyNotices'),
	url(r'^faccalender/$', views.faccalender , name = 'faccalender'),
	url(r'^studcalender/$', views.studcalender , name = 'studcalender'),


]
