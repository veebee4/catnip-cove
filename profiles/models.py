from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining records of
    donations and giving access to registered users blog
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    default_last_name = models.CharField(max_length=100, blank=True, null=True)
    default_email_address = models.EmailField(
        max_length=100,
        blank=True,
        null=True
    )
    default_postcode = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # existing users - just save profile
        instance.userprofile.save()
