# creating the url patterns for model

from django.urls import path

from . import views 


app_name = 'note_logs' # this naming helps django to identify this file

urlpatterns = [
	# Home page
	path('', views.index, name='index'),
		#	this will call the index method in views.py to
		#	show the home page.
		#	The name is a pattern for the url, so at anytime
		#	we can refer to it by its name. 
	path('notepads/', views.notepads, name='notepads')
]