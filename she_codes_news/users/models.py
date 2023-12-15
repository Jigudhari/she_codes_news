from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    profile_picture = models.URLField(null=True, blank=True)
    pass 

    def __str__(self):
        return self.username
