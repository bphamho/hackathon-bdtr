from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length = 200)
    write_date = models.DateTimeField('date published')
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length = 400)
    
class Comment(models.Model):
    commentor = models.CharField(max_length = 200)
    write_date = models.DateTimeField('date published')

class Video(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length = 200)
    videofile= models.FileField(upload_to='videos//%y')
    post_date = models.DateTimeField('date published')
         
    def __str__(self):
        return self.title
     