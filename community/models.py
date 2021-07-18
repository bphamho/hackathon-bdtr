from django.db import models
from django.contrib.auth.models import User
from forum.models import Post
from PIL import Image

class CommunityDetail(models.Model):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=300)
    founder = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    image = models.ImageField(default="no_image.png", upload_to="images/community")
    members = models.ManyToManyField(User, related_name='community_members')
    posts = models.ManyToManyField(Post, related_name="community_posts")

    def __str__(self):
        return str(self.name)
        
    #def save(self, *args, **kwargs):
    
        #super().save(*args, **kwargs)
        #community_image = Image.open(self.image.name)
        
        #max_height = 400
        #max_width = 200
        #max_size = (max_height, max_width)
        
        #if community_image.height > max_height or community_image.width > max_width:
            #community_image.thumbnail(max_size)
            #community_image.save(self.image.name)