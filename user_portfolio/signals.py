from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from .models import Profile, LoggedInUsers

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print( f"User \"{user.username}\" logged in" )
    LoggedInUsers.objects.create(user=user)
 
@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    print( f"User \"{user.username}\" logged out" )
    logged_in = LoggedInUsers.objects.filter(user=user)
    for u in logged_in:
        u.delete()
