from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from ckeditor.fields import RichTextField

# Some fairly simple error handling in the Managers below
# which will allow you to launch the application without
# any content in the database - using the ObjectDoesNotExist
# exception to check if there is anything in the database to display

class PublishedManager(models.Manager):
	use_for_related_fields = True

	def published(self, **kwargs):
		try:
			results = self.get(visibility='Published', **kwargs)
		except ObjectDoesNotExist:
			results = None
		return results

class PublishedListManager(models.Manager):
	use_for_related_fields = True

	def all_published(self, **kwargs):
		try:
			results = self.filter(visibility='Published', **kwargs).order_by('display_order')
		except ObjectDoesNotExist:
			results = None
		return results

class TimeStampModel(models.Model):
	"""This is a meta model class - it puts created
	and modified fields on every model that inherits
	from it"""
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True

class Visibility(models.Model):
	"""This meta model is used for adding publishe
	elements to all models for visibility purposes"""
	PUBLISHED = 'Published'
	UNPUBLISHED = 'Unpusblished'
	VISIBILITY_CHOICES = (
		(PUBLISHED, 'Published'),
		(UNPUBLISHED, 'Unpusblished')
	)
	display_order = models.IntegerField()
	visibility = models.CharField(max_length=20,
								  choices=VISIBILITY_CHOICES,
								  default=UNPUBLISHED)
	class Meta:
		abstract = True
			