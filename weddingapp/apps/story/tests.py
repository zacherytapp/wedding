from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse 

from story.models import Story, Timeline

class StoryTest(TestCase):
	
	def setUp(self):
		Story.objects.get_or_create(title="story1", 
									story_body="test body",
									visibility="Published",
									display_order="1")
		Timeline.objects.get_or_create(title="timeline1", 
										timeline_description="test body",
										link_title="test",
										button_link="http://www.google.com",
										show_button=True,
										visibility="Published",
										display_order="1" )
		Timeline.objects.get_or_create(title="timeline2", 
										timeline_description="test body2",
										link_title="test",
										button_link="http://www.google.com",
										show_button=True,
										visibility="Published",
										display_order="2" )

	# Sanity check that stuff is loading in the view.
	def test_base_template_used(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertTemplateUsed(response, 'base.html' )
		self.assertTemplateUsed(response, 'story_detail.html')

	# Ensure that published and unpublished stuff dispaly correctly.
	def test_check_published_ability(self):
		published_story = Story.objects.filter(visibility='Published').count()
		unpublished_timeline = Timeline.objects.filter(visibility='Unpublished').count()
		
		self.assertEqual(published_story, 1)
		self.assertEqual(unpublished_timeline, 0)

	# Test that the published story actually show in the view.
	def test_published_manager(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertEqual(len(response.context['timeline']), 2)