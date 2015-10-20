from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from story.models import Story, Timeline
from gallery.models import Gallery
from party.models import PartyMember
from information.models import InformationDetail
from travel.models import Hotel, TravelDetail
from contact.models import Contact
from registry.models import Registry
from contact.forms import ContactForm

# This view renders the main page while passing in
# a bunch of contexts for display in the templates.
# You can check out how to use get_context_data here:
# https://docs.djangoproject.com/en/1.8/ref/class-based-views/mixins-simple/

class HomeView(TemplateView):
	template_name = "base.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['story'] = Story.objects.published()
		context['gallery'] = Gallery.objects.all_published()
		context['timeline'] = Timeline.objects.all_published()
		context['party_member'] = PartyMember.objects.all_published()
		context['information_detail'] = InformationDetail.objects.published()
		context['travel_detail'] = TravelDetail.objects.published()
		context['hotel'] = Hotel.objects.all_published()
		context['registry'] = Registry.objects.all_published()
		context['form'] = ContactForm
		return context
