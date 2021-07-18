from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
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
