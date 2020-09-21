from django.shortcuts import render

from .models import Notepad

# Create your views here.

def index(request):
	# the function to manage the home page of the web project
	return render(request, 'note_logs/index.html') # the name of the template

def notepads(request):
	# this function gets the notepads and will send them to template to render
	notepads = Notepad.objects.order_by('date_added')	
	context = {'notepads': notepads} # this part is up to us to send whatever
									 # we want to the template
	return render(request, 'note_logs/notepads.html', context)

def notepad(request, topic_id):
	# this function shows the notes of a notepad
	notepad = Notepad.objects.get(id=topic_id)
	notes = notepad.note_set.order_by('-date_added') # get the notes
	context = {'notepad': notepad, 'notes': notes} # create the context	
	return render(request, 'note_logs/notepad.html', context)