from django.forms import ModelForm
from django import forms
from django.forms import widgets
from django.forms.widgets import TextInput, EmailInput, Textarea
from .models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['full_name', 'email', 'message']
		widgets = {
            'full_name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'message': Textarea(attrs={'class': 'form-control'})
        }