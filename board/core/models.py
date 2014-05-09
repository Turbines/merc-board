from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"

    email = models.EmailField(unique=True)

