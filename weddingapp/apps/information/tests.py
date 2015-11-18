from django.test import TestCase
from django.core.urlresolvers import reverse 

from information.models import InformationDetail

class InformationTests(TestCase):

	def test_empty_info_db(self):
		no_info = InformationDetail.objects.filter(visibility='Published').count()

		self.assertEqual(no_info, 0)

	# Test that the two published events actually show in the view.
	def test_published_manager_none(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertEqual(response.context['information_detail'], None)
		

	def test_published_manager(self):
		InformationDetail.objects.get_or_create(title="info1", 
												body="Test Body",
												visibility="Published",
												display_order="1" )

		published_info = InformationDetail.objects.filter(visibility="Published").count()
		unpublished_info = InformationDetail.objects.filter(visibility="Unpublished").count()

		self.assertEqual(published_info, 1)
		self.assertEqual(unpublished_info, 0)

