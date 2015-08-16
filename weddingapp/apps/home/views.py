from django.shortcuts import render
from django.views.generic import TemplateView

from story.models import Story

# This view renders the main page while passing in
# a bunch of contexts for display in the templates.
# You can check out how to use get_context_data here:
# https://docs.djangoproject.com/en/1.8/ref/class-based-views/mixins-simple/

class HomeView(TemplateView):
	template_name = "base.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['story'] = Story.objects.published()
		return context