from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from core.behaviors import TimeStampModel, Visibility, PublishedManager, PublishedListManager

class InformationDetail(TimeStampModel, Visibility):
	title = models.CharField(max_length=50)
	body = RichTextField(config_name='awesome_ckeditor')
	
	objects = PublishedManager()
