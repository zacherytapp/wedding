from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse 

from .models import Event

class EventsTest(TestCase):

	def setUp(self):
		Event.objects.get_or_create(title="event1", 
									date_time="9/1/2011",
									description="eventdescription1",
									visibility="Published",
									display_order="1" )
		Event.objects.get_or_create(title="event2", 
									date_time="9/1/2012",
									description="eventdescription2",
									visibility="Published",
									display_order="2" )
		Event.objects.get_or_create(title="event3", 
									date_time="9/1/2012",
									description="eventdescription3",
									visibility="Unpublished",
									display_order="3" )

	# Sanity check test
	def test_base_template_used(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertTemplateUsed(response, 'base.html' )
		self.assertTemplateUsed(response, 'events.html')

	def test_check_published_ability(self):
		published_events = Event.objects.filter(visibility='Published').count()

		self.assertEqual(published_events, 2)

	def test_published_manager(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertEqual(len(response.context['event']), 2)




