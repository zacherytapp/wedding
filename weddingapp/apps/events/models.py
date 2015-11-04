from django.db import models
from ckeditor.fields import RichTextField
from core.behaviors import TimeStampModel, Visibility, PublishedManager, PublishedListManager

class Event(TimeStampModel, Visibility):
	title = models.CharField(max_length=100)
	date_time = models.CharField(max_length=150)
	description = RichTextField(config_name='awesome_ckeditor')

	objects = PublishedListManager()