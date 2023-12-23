from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_image = models.ImageField(verbose_name='photo de profil')

