from django.conf import settings
from django.db import models


class Mercenary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)


class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

