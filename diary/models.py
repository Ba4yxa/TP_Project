from django.conf import settings
from django.db import models
from django.utils import timezone

class record(models.Model):
    title = models.CharField(max_length=20)
    rating = models.SmallIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    create_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    
    def __str__(self):
        return self.title
    
    