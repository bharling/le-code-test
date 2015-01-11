from django.test import TestCase

# Create your tests here.


class StreamViewTest(TestCase):
    def test_can_visit_stream_page(self):
        response = self.client.get('/stream')
        self.assertEqual(response.status_code, '200', 'Could not load stream page')