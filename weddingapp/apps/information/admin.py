from django.contrib import admin

from .models import InformationDetail

class InformationAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'display_order', 'visibility')
	search_fields = ['title', 'body']

admin.site.register(InformationDetail, InformationAdmin)