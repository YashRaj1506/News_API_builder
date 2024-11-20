from django.db import models

# Create your models here.

class News_data(models.Model):
    # CATEGORY_CHOICES = [
    #     ('sports', 'Sports'),
    #     ('politics', 'Politics'),
    #     ('technology', 'Technology'),
    #     ('economy', 'Economy'),
    # ]
    title = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.title

