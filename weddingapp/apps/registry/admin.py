from django.contrib import admin

from .models import Registry

class RegistryAdmin(admin.ModelAdmin):
	list_display = ('title', 'alt_text', 'display_order', 'visibility')
	search_fields = ['title', 'alt_text']

admin.site.register(Registry, RegistryAdmin)
