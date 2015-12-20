from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Story, Timeline

class StoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'story_body', 'display_order', 'visibility')
	search_fields = ['title', 'story_body']

class TimelineAdmin(admin.ModelAdmin):
	list_display = ('title', 'timeline_date', 'display_order', 'visibility')
	search_fields = ['title', 'timeline_description', 'timeline_date']

admin.site.register(Story, StoryAdmin)
admin.site.register(Timeline, TimelineAdmin)
