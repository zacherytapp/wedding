from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
	use_for_related_fields = True

	def published(self, **kwargs):
		return self.get(visibility='Published', **kwargs)

class TimeStampModel(models.Model):
	"""This is a meta model that other models 
	will inherit from"""
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True

class Visibility(models.Model):
	"""This is a meta model that other models
	will inherit from - it's used for adding
	publish elements to all models"""
	PUBLISHED = 'Published'
	UNPUBLISHED = 'Unpublished'
	VISIBILITY_CHOICES = (
    	(PUBLISHED, 'Published'),
    	(UNPUBLISHED, 'Unpublished')
    )
	display_order = models.IntegerField()
	visibility = models.CharField(max_length=20,
                                  choices=VISIBILITY_CHOICES,
                                  default=UNPUBLISHED)
	class Meta:
		abstract = True
			
