from django.db.models.signals import post_save      #signal fired when object is saved 
from django.contrib.auth.models import User         #sender
from django.dispatch import receiver                #receiver
from .models import Profile                         #help create profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ino = Profile.objects.create(user=instance)
        ino.save()
    


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()