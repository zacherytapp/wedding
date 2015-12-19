from django.contrib import admin

from .models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_time', 'display_order', 'visibility')
	search_fields = ['title', 'date_time', 'description']

admin.site.register(Event, EventAdmin)