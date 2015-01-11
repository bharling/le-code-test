from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.


class StreamViewTest(TestCase):
    fixtures = ['stream.json']
    
    def test_stream_page_exists(self):
        response = self.client.get(reverse('stream'))
        self.assertEqual(response.status_code, 200, 'Could not load stream page')    
        self.assertContains(response, 'Your Stream')
        
    def test_stream_page_has_items(self):
        response = self.client.get(reverse('stream'))
        self.assertNotEqual(response.context['stream'], [], 'Stream Queryset is empty')