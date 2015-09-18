from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from core.behaviors import TimeStampModel, Visibility, PublishedManager, PublishedListManager

# Be sure to check the behaviors.py in this app
# to see the rest of this model's functionality

class Story(TimeStampModel, Visibility):
	title = models.CharField(max_length=200)
	story_body = RichTextField(config_name='awesome_ckeditor')

	objects = PublishedManager()

class Timeline(TimeStampModel, Visibility):
	title = models.CharField(max_length=200)
	timeline_description = RichTextField(config_name='awesome_ckeditor')
	timeline_date = models.CharField(max_length=50)
	link_title = models.CharField(max_length=200, blank=True)
	button_link = models.URLField(max_length=500, blank=True)
	show_button = models.BooleanField()

	objects = PublishedListManager()
		

	
		
