from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Story, Timeline

admin.site.register(Story)
admin.site.register(Timeline)
