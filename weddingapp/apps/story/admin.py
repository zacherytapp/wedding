from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Story, Timeline

# Register your models here.

admin.site.register(Story)
admin.site.register(Timeline)
