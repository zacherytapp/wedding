from django.test import TestCase

from django.core.urlresolvers import reverse 

class HomeTest(TestCase):

	def test_home_page_load(self):
		url = reverse('home')
		response = self.client.get(url) 
		self.assertEquals(response.status_code, 200)