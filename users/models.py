from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager
from django.utils.translation import gettext as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None

    objects = CustomUserManager()

    def __str__(self):
        return self.email

