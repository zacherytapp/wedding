from django.db import models
from ckeditor.fields import RichTextField
from core.behaviors import TimeStampModel, Visibility, PublishedManager, PublishedListManager

class PartyMember(TimeStampModel, Visibility):
	BRIDE = 'Bride'
	GROOM = 'Groom'
	GROOMSMAN = 'Groomsman'
	BRIDESMAID = 'Bridesmaid'
	BEST_MAN = 'Best Man'
	MAID_OF_HONOR = 'Maid of Honor'
	MATRON_OF_HONOR = 'Matron of Honor'
	USHER = 'Usher'
	OFFICIANT = 'Officiant'
	PUBLISHED = 'Published'
	UNPUBLISHED = 'Unpublished'
	MEMBER_ROLE_CHOICES = (
		(BRIDE, "Bride"),
		(GROOM, "Groom"),
		(GROOMSMAN, "Groomsman"),
		(BRIDESMAID, "Bridesmaid"),
		(BEST_MAN, "Best Man"),
		(MAID_OF_HONOR, "Maid of Honor"),
		(MATRON_OF_HONOR, "Matron of Honor"),
		(USHER, "Usher"),
		(OFFICIANT, "Officiant")
	)

	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	location = models.CharField(max_length=100)
	description = RichTextField(config_name='awesome_ckeditor')
	image = models.ImageField(max_length=100)
	alt_text = models.CharField(max_length=200)
	role = models.CharField(max_length=20,
                                    choices=MEMBER_ROLE_CHOICES,
                                    default=BRIDE)

	objects = PublishedListManager()