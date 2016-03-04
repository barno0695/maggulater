from django.conf.urls import url


from . import views 

urlpatterns = [
	url(r'^login/$', views.login, name = 'login'),
	url(r'^signUp/$', views.signUp, name = 'signUp'),
	url(r'^Home/$', views.Home , name = 'Home'),
	url(r'^index/$' , views.home, name = 'Index'),

]