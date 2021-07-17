from django.db import models
from django.contrib.auth.models import User

class CommunityDetail(models.Model):
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=300)
    founder = models.ForeignKey(User, on_delete=models.CASCADE, default = None)
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return str(self.name)
