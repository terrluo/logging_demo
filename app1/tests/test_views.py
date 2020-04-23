from django.test import TestCase
from django.urls import reverse


class App1ListViewTestCase(TestCase):
    def test_get(self):
        resp = self.client.get(reverse('app1:list'))
        self.assertEqual(resp.status_code, 200)
