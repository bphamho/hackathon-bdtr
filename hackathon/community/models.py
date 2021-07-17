from django.db import models
from django.contrib.auth.models import User

class CommunityDetail(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.name)
