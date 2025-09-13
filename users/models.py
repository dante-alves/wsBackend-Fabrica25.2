from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    photo = models.ImageField(default='fallback_user.png', blank=True)