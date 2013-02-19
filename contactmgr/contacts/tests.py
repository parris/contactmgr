"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import RequestFactory
from django.test.client import Client

from contacts.models import Contact
from contacts.views import ListContactsView


class ContactTests(TestCase):

    def test_str(self):

        c = Contact(first_name='Parris', last_name='Khachi')
        self.assertEqual(str(c), 'Parris Khachi')


class ContactListViewTests(TestCase):

    def test_contacts_in_the_context(self):

        client = Client()
        response = client.get('/')

        self.assertEquals(list(response.context['object_list']), [])

        Contact.objects.create(first_name='foo', last_name='bar')
        response = client.get('/')

        self.assertEquals(response.context['object_list'].count(), 1)

    def test_contacts_in_the_context_request_factory(self):

        factory = RequestFactory()
        request = factory.get('/')

        response = ListContactsView.as_view()(request)

        self.assertEquals(list(response.context_data['object_list']), [])

        Contact.objects.create(first_name='foo', last_name='bar')
        response = ListContactsView.as_view()(request)
        self.assertEquals(response.context_data['object_list'].count(), 1)
