from django.shortcuts import render, redirect

from .models import Notepad, Note
from .forms import NotepadForm, NoteForm

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
	# this function adds a new notepad to the database for a user
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

def new_note(request, notepad_id):
	# this function creates and adds a new note to database for a user
	notepad = Notepad.objects.get(id=notepad_id)
	if request.method != 'POST':
		# no data submited
		form = NoteForm()
	else:
		# process the given data
		form = NoteForm(data=request.POST)
		if form.is_valid():
			# save after validation
			new_note = form.save(commit=False)
			new_note.notepad = notepad
			new_note.save()
			# at first we tell django to create a space for the new note but
			# not save it to database, after we defined the notepad of the note
			# we save it into the database with its notepad.
			return redirect('note_logs:notepad', notepad_id=notepad_id)
	# display a blank or invalid form page
	context = {'notepad': notepad, 'form': form}
	return render(request, 'note_logs/new_note.html', context)		

def edit_note(request, note_id):
	# this function is for editing a choosen note
	note = Note.objects.get(id=note_id)
	notepad = note.notepad
	if request.method != 'POST':
		# no data submited
		form = NoteForm(instance=note) # this argument allows the users to see
									   # their data.
	else:
		# process the given data
		form = NoteForm(instance=note, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('note_logs:notepad', notepad_id=notepad.id)
	context = {'note': note, 'notepad': notepad, 'form': form}
	# display a blank or invalid form page
	return render(request, 'note_logs/edit_note.html', context)		

def delete_notepad(request, notepad_id):
	# this function deletes a notepad of a user
	context = {'result': ''}
	try:
		# if the notepad did not exists
		notepad = Notepad.objects.get(id=notepad_id)
		notepad.delete()
		context['result'] = "OK"
	except Notepad.DoesNotExist:
		context['result'] = "FAILD"
	return render(request, 'note_logs/remove_result.html', context)		

def delete_note(request, note_id):
	# this function deletes a note for user
	context = {'result': ''}
	try:
		# if the note did not exists
		note = Note.objects.get(id=note_id)
		note.delete()
		context['result'] = "OK"
	except Note.DoesNotExist:
		context['result'] = "FAILD"
	return render(request, 'note_logs/remove_result.html', context)	