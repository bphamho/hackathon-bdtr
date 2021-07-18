from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length = 200)
    write_date = models.DateTimeField('date published')
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length = 5000)