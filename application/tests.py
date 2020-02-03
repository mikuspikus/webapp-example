from django.test import TestCase, Client
from django.urls import reverse

from . import models

class ApplicationTests(TestCase):
    model = models.Application
    client = Client()

    def test_big_name(self):
        data = {'name' : 'a' * 256, 'surname': 'b', 'phone' : 'c'}

        response = self.client.post(reverse('application:index'), data = data)
        self.assertEqual(response.status_code, 400)

    def test_good_name(self):
        data = {'name' : 'a' * 126, 'surname': 'b', 'phone' : 'c'}

        response = self.client.post(reverse('application:index'), data = data)
        self.assertEqual(response.status_code, 302)
