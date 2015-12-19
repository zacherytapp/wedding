from django.contrib import admin

from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
	list_display = ('title', 'gallery_image', 'alt_text', 'display_order', 'visibility')
	search_fields = ['title', 'alt_text']

admin.site.register(Gallery, GalleryAdmin)