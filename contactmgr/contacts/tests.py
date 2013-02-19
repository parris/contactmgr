"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from contacts.models import Contact

class ContactTests(TestCase):
	
	def test_str(self):
		c= Contact(first_name='Parris', last_name='Khachi')
                self.assertEqual(str(c), 'Parris Khachi')
		

class SimpleTest(TestCase):
	def test_basic_addition(self):
		"""
		Tests that 1 + 1 always equals 2.
        	"""
		self.assertEqual(1 + 1, 2)
