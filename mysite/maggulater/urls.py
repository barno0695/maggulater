from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signUp/$', views.signUp, name = 'signUp'),
	# url(r'^index/$' , views.home, name = 'Index'),
	url(r'^faculty/$' , views.faculty, name = 'faculty'),
	url(r'^home/$', views.home , name = 'home'),
	url(r'^profile/$', views.profile , name = 'profile'),
	# url(r'^index/$' , views.home, name = 'Index'),

]
