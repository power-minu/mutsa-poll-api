from django.db import models

# Create your models here.

class Poll(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)