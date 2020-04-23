from django.test import TestCase

from app1.models import App1


class ModelsTestCase(TestCase):
    def test_str(self):
        app = App1.objects.create(name='1')
        self.assertEqual(app.__str__(), '1')
