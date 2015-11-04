from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Contact
from .forms import ContactForm
from home.views import HomeView

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class ContactCreate(AjaxableResponseMixin, CreateView):
    model = Contact
    fields = ('full_name', 'email', 'message')
    success_msg = "Contact form submitted!"
    success_url = "/contact_success/"

    def form_invalid(self, form):
        return render_to_response('base.html')

class ContactSuccessView(TemplateView):
	template_name = 'contact_success.html'