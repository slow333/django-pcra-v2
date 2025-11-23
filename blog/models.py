from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # () 없음.
    date_updated = models.DateTimeField(auto_now=True) #add를 하면 update에 대해 처리함
    # date_updated = models.DateTimeField(auto_now_add=True) #add를 하면 update에 대해 처리함
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})