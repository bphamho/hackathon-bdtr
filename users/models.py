from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from community.models import CommunityDetail
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    about_me = models.TextField(max_length=200, blank=True)
    date_joined = models.DateField(default=timezone.now)
    image = models.ImageField(default='default_profile.png', upload_to='profile_pictures')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     profile_picture = Image.open(self.image.path)
        
    #     max_height = 400
    #     max_width = 200
    #     max_size = (max_height, max_width)
        
    #     if profile_picture.height > max_height or profile_picture.width > max_width:
    #         profile_picture.thumbnail(max_size)
    #         profile_picture.save(self.image.path)
