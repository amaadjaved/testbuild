from django.test import TestCase
from web.models import Web

class AnimalTestCase(TestCase):
    def setUp(self):
        Web.objects.create(url="http://google.com")

    def test_url_google(self):
        google = Web.objects.get(url="http://google.com")
        self.assertEqual(google.url, 'http://google.com')
