from django.test import TestCase

class HealthCheckTest(TestCase):

    def test_index(self):
        self.assertEqual(self.client.get('/').status_code, 200)
