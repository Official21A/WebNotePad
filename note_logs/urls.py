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
	path('notepads/', views.notepads, name='notepads'),
	# Each notepad notes 
	path('notepads/<int:notepad_id>/', views.notepad, name='notepad'),
	# Page for adding new notepad
	path('new_notepad/', views.new_notepad, name='new_notepad'),
	# Page for adding new note
	path('new_note/<int:notepad_id>/', views.new_note, name='new_note'),
	# Page for editing a note
	path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
	# Page for deleting a note
	path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
]
