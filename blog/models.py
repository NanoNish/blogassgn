from django.conf import settings
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=200, primary_key=True, null = False, unique = True)
    password = models.CharField(max_length=200, null = False)
    email = models.CharField(max_length=200)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null = False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title