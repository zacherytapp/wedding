from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from core.behaviors import TimeStampModel, Visibility, PublishedManager, PublishedListManager

class Contact(TimeStampModel):
	full_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=150)
	message = models.TextField(max_length=5000)
