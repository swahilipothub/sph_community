from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, 
        related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to = 'assets/images',
        default = 'no-img.jpg',
        blank=True
    )
    mobile_number = models.CharField(max_length=13, blank=True)
    birth_date = models.DateField(default='1999-12-31')
    bio = models.TextField(default='')
    location = models.CharField(max_length=256, default='')
    city = models.CharField(max_length=256, default='')
    county = models.CharField(max_length=256, default='')
    country = models.CharField(max_length=256, default='')
    facebook = models.CharField(max_length=256, blank=True, default='')
    twitter = models.CharField(max_length=256, blank=True, default='')
    linkedin = models.CharField(max_length=256, blank=True, default='')
    youtube = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile', args=(self.pk,))

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_uer_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()