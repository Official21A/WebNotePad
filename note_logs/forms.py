from django import forms

from .models import Notepad


class NotepadForm(forms.ModelForm):
	# the base form class
	class Meta:
		# this will tell django to set the base in form of which class
		# and which fields to include in the form
		model = Notepad
		fields = ['text']
		labels = {'text': ''}