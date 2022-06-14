
from django.db import models
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)
