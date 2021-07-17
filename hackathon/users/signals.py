<<<<<<< HEAD
=======
  
>>>>>>> 5dbb1683cf5bd2c2ac0bbb2b7ad7f262778d732f
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
<<<<<<< HEAD
    instance.userprofile.save()
=======
    instance.userprofile.save()
>>>>>>> 5dbb1683cf5bd2c2ac0bbb2b7ad7f262778d732f
