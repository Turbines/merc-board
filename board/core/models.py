from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.db import models


class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    objects = UserManager()


class Mercenary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

