from django.test import TestCase

from django.core.urlresolvers import reverse 

class HomeTest(TestCase):

	# Sanity check to ensure that the home page resolves.
	def test_home_page_load(self):
		url = reverse('home')
		response = self.client.get(url) 
		self.assertEquals(response.status_code, 200)

	# This test ensures that all the templates are getting loaded
	# into the view properly.
	def test_base_template_used(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertTemplateUsed(response, 'base.html' )
		self.assertTemplateUsed(response, 'contact.html')
		self.assertTemplateUsed(response, 'events.html')
		self.assertTemplateUsed(response, 'gallery.html')
		self.assertTemplateUsed(response, 'header.html')
		self.assertTemplateUsed(response, 'information.html')
		self.assertTemplateUsed(response, 'nav.html')
		self.assertTemplateUsed(response, 'registry.html')
		self.assertTemplateUsed(response, 'story_detail.html')
		self.assertTemplateUsed(response, 'travel.html')
		self.assertTemplateUsed(response, 'wedding_party.html')