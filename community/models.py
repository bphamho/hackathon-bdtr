from django.db import models
from django.contrib.auth.models import User
from forum.models import Post
from PIL import Image

class CommunityDetail(models.Model):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=300)
    image = models.ImageField(default="no_image.png", upload_to="community")
    founder = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    members = models.ManyToManyField(User, related_name='community_members')
    posts = models.ManyToManyField(Post, related_name="community_posts")

    def __str__(self):
        return str(self.name)
