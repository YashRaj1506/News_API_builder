from django.db import models

# Create your models here.

class News_data(models.Model):
    CATEGORY_CHOICES = [
        ('sports', 'Sports'),
        ('politics', 'Politics'),
        ('technology', 'Technology'),
    ]
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='news')
    content = models.CharField(max_length=5000)

