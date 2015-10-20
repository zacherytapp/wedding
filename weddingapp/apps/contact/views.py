from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Contact
from .forms import ContactForm

class ContactActionMixin(object):
	fields = ('full_name', 'email', 'message')

	@property
	def success_msg(self):
	    return NotImplemented

	def form_valid(self, form):
		messages.info(self.request, self.success_msg)
		return super(ContactActionMixin, self).form_valid(form)


class ContactCreate(ContactActionMixin, CreateView):
    model = Contact
    success_msg = "Contact form submitted!"

class ContactSuccessView(TemplateView):
	template_name = 'contact_success.html'
