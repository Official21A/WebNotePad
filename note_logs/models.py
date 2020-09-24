from django.db import models
from django.contrib.auth.models import User

import datetime
import pytz

# Create your models here.


class Notepad(models.Model):
    # the notepad class which contains notes
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # above var shows each notepad for 
    # a user so just that user can get access to it.

    def __str__(self):
        # a method for django to show the users the topic
        return self.text
        

class Note(models.Model):
    # the note class where the user enters its notes
    notepad = models.ForeignKey(Notepad, on_delete=models.CASCADE)
    # above var is for database to connect each Note to its own Notepad
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modify = models.DateTimeField()

    class Meta:
    	# this inner class will let us add more details about a class for django
    	verbose_name_plural = 'notes'

    def __str__(self):
    	# a method for django to show the users the topic
    	return f"{self.text[:50]}..."	
        		        