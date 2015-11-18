from django.test import TestCase, Client

from contact.models import Contact

class ContactTest(TestCase):

	def setUp(self):
		Contact.objects.get_or_create(full_name="Test Contact", 
									  email="test@gmail.com",
									  message="Test Message",)
		Contact.objects.get_or_create(full_name="Test Contact1", 
									  email="test1@gmail.com",
									  message="Test Message1",)
		Contact.objects.get_or_create(full_name="Test Contact2", 
									  email="test2@gmail.com",
									  message="Test Message2",)

	def test_contact_create(self):
		all_contacts = Contact.objects.all().count()

		self.assertEqual(all_contacts, 3)

