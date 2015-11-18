from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse 

from events.models import Event

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

	# Sanity check that stuff is loading in the view.
	def test_base_template_used(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertTemplateUsed(response, 'base.html' )
		self.assertTemplateUsed(response, 'events.html')

	# Ensure that published and unpublished events dispaly correctly.
	def test_check_published_ability(self):
		Event.objects.get_or_create(title="event4", 
									date_time="9/1/2011",
									description="eventdescription4",
									visibility="Published",
									display_order="4" )

		published_events = Event.objects.filter(visibility='Published').count()
		unpublished_events = Event.objects.filter(visibility='Unpublished').count()
		second_event = Event.objects.get(title="event2")

		
		self.assertEqual(published_events, 3)
		self.assertEqual(unpublished_events, 1)
		self.assertEqual(first_event[0].title, "event1")
		self.assertEqual(second_event.title, "event2")


	# Test that the two published events actually show in the view.
	def test_published_manager(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertEqual(len(response.context['event']), 2)




