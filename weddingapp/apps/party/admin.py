from django.contrib import admin

from .models import PartyMember

class PartyAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'role', 'display_order', 'visibility')
	search_fields = ['first_name', 'last_name', 'role', 'description', 'alt_text']

admin.site.register(PartyMember, PartyAdmin)
