from django.contrib import admin

from .models import Hotel, TravelDetail

class HotelAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'display_order', 'visibility')
	search_fields = ['title', 'description']

class TravelAdmin(admin.ModelAdmin):
	list_display = ('title', 'body', 'display_order', 'visibility')
	search_fields = ['title', 'body']

admin.site.register(Hotel, HotelAdmin)
admin.site.register(TravelDetail, TravelAdmin)
