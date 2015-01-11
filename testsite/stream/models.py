from django.db import models
from django.contrib.auth.models import User
from items.models import PhotoItem, TweetItem
from django.core.exceptions import ValidationError

class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField()
    tweet = models.ForeignKey(TweetItem, null=True, blank=True, related_name="streams")
    photo = models.ForeignKey(PhotoItem, null=True, blank=True, related_name="streams")
    
    @property
    def deleted(self):
        if self.tweet:
            return self.tweet.deleted
        if self.photo:
            return self.photo.deleted
    
    def clean(self):
        if self.tweet is None and self.photo is None:
            raise ValidationError('A Stream Item must have either a Tweet or a Photo')
        if self.tweet and self.photo:
            raise ValidationError('A stream Item cannot have both a Tweet AND a Photo')
        
    class Meta:
        ordering = ['-created_at']
            