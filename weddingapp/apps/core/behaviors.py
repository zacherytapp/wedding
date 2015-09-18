from django.db import models
from django.utils import timezone

from ckeditor.fields import RichTextField

class PublishedManager(models.Manager):
	use_for_related_fields = True

	def published(self, **kwargs):
		return self.get(visibility='Published', **kwargs)

class PublishedListManager(models.Manager):
	use_for_related_fields = True

	def all_published(self, **kwargs):
		return self.filter(visibility='Published', **kwargs).order_by('display_order')

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
			