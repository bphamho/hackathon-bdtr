from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length = 200)
    write_date = models.DateTimeField('date published')
    title = models.CharField(max_length = 200)
    content = models.CharField(max_length = 400)
   # community = models.ForeignKey(Community)

class Comment(models.Model):
    commentor = models.CharField(max_length = 200)
    write_date = models.DateTimeField('date published')
    comment = models.CharField(max_length = 400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class Video(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length = 200)
    videofile= models.FileField(upload_to='videos//%y', null=True)
    post_date = models.DateTimeField('date published')
         
    def __str__(self):
        return self.title
