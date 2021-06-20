from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200, blank=True)
    language = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    time = models.CharField(max_length=10, blank=True)
    deadline = models.CharField(max_length=10, blank=True)
    user = models.CharField(max_length=50)
    
