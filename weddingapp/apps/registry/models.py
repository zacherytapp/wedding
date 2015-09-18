from django.db import models

from core.behaviors import TimeStampModel, Visibility, PublishedListManager

class Registry(TimeStampModel, Visibility):
	title = models.CharField(max_length=50)
	alt_text = models.CharField(max_length=200)
	registry_image = models.ImageField(max_length=100)

	objects = PublishedListManager()
