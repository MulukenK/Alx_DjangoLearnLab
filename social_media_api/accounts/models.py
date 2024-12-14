from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

    def __str__(self):
        return self.username


class User(AbstractUser):
    # Adding 'following' to track users that a user follows
    following = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
