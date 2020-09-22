from django.shortcuts import render, redirect

from .models import Notepad
from .forms import NotepadForm

# Create your views here.

def index(request):
	# the function to manage the home page of the web project
	return render(request, 'note_logs/index.html') # the name of the template

def notepads(request):
	# this function gets the notepads and will send them to template to render
	notepads = Notepad.objects.order_by('date_added')	
	context = {'notepads': notepads} # this part is up to us to send whatever
									 # we want to the template.
	return render(request, 'note_logs/notepads.html', context)

def notepad(request, notepad_id):
	# this function shows the notes of a notepad
	notepad = Notepad.objects.get(id=notepad_id)
	notes = notepad.note_set.order_by('-date_added') # get the notes
	context = {'notepad': notepad, 'notes': notes} # create the context	
	return render(request, 'note_logs/notepad.html', context)

def new_notepad(request):
	# this function adds a new notepad to the database of a user
	if request.method != 'POST':
		# no data submited
		form = NotepadForm()
	else:
		# process the data
		form = NotepadForm(data=request.POST)
		if form.is_valid():
			# check the input validation
			form.save()
			return redirect('note_logs:notepads') # this will take user back to
												  # the notepads page.
	# display a blank or invalid form page
	context = {'form': form}
	return render(request, 'note_logs/new_notepad.html', context)				