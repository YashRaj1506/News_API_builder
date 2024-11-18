from django.db import models

# Create your models here.

class News_data(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    content = models.TextField()
