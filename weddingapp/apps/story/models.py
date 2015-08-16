from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from behaviors import TimeStampModel, Visibility, PublishedManager

# Be sure to check the behaviors.py in this app
# to see the rest of this model's functionality

class Story(TimeStampModel, Visibility):
	title = models.CharField(max_length = 200)
	story_body = RichTextField(config_name='awesome_ckeditor')

	objects = PublishedManager()


	
		
