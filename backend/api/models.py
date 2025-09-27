from django.db import models
from django.contrib.auth.models import AbstractUser

# Update in settings.py
class CustomUser(AbstractUser):
    major = models.TextField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username

