from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=0)

    def __str__(self):
        return self.title
# models.py
from django.db import models

class MetaModel(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view", "Can view model instances"),
            ("can_create", "Can create model instances"),
            ("can_edit", "Can edit model instances"),
            ("can_delete", "Can delete model instances"),
        ]

    def str(self):
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    email = models.EmailField(unique=True)

    objects = CustomUserManager()

    def str(self):
        return self.email