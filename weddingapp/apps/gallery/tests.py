import os
import mock

from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse 
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from django.core.files.storage import Storage

from gallery.models import Gallery

class GalleryTests(TestCase):

	def setUp(self):
		newGallery = Gallery()
		newGallery.gallery_image = SimpleUploadedFile(name='dan-hill.jpg', content=open('/Users/ZacheryTapp/weddingapp/weddingapp/weddingapp/weddingapp/assets/img/dan-hill.jpg', 'rb').read(), content_type='image/jpeg')
		newGallery.title = "gallery1"
		newGallery.alt_text = "gallery alt 1"
		newGallery.visibility = "Published"
		newGallery.display_order = "1"
		newGallery.save()

	# Sanity check that stuff is loading in the view.
	def test_base_template_used(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertTemplateUsed(response, 'base.html' )
		self.assertTemplateUsed(response, 'gallery.html')

	def test_add_new_gallery(self):
		self.assertEqual(Gallery.objects.count(), 1)

	def test_published_gallery(self):
		published_gallery = Gallery.objects.filter(visibility="Published").count()
		unpublished_gallery = Gallery.objects.filter(visibility="Unpublished").count()

		self.assertEqual(unpublished_gallery, 0)
		self.assertEqual(published_gallery, 1)

	def test_published_manager(self):
		url = reverse('home')
		response = self.client.get(url)

		self.assertEqual(len(response.context['gallery']), 1)

