from django.test import TestCase
from django.core.urlresolvers import reverse
import datetime
from stream.models import Stream
from items.models import PhotoItem, TweetItem
from django.contrib.auth.models import User

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
        
    def test_stream_page_displays_an_image(self):
        response = self.client.get(reverse('stream'))
        self.assertContains(response, '<img')
        
    def test_stream_page_displays_a_known_tweet(self):
        user = User.objects.first()
        tweet = TweetItem.objects.create(user=user, created_at=datetime.datetime.now(), text="Bongo")
        stream_item = Stream.objects.create(user=user, created_at=datetime.datetime.now(), tweet=tweet)
        response = self.client.get(reverse('stream'))
        self.assertContains(response, tweet.text)
        
    