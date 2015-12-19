from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'email')
	search_fields = ['full_name', 'email', 'message']

admin.site.register(Contact, ContactAdmin)
