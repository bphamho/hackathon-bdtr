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
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class AddCommentButton(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    
class CommentBox(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 400)