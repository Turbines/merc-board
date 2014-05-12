from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone


class UserManager(auth_models.UserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **kwargs):
        now = timezone.now()

        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=True,
                          date_joined=now, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(auth_models.AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    objects = UserManager()


class Mercenary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

