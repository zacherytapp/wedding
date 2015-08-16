from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Story

# Register your models here.

admin.site.register(Story)
