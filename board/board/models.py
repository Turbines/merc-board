from annoying.fields import AutoOneToOneField
from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MercenaryProfile(BaseModel):
    user = AutoOneToOneField(settings.AUTH_USER_MODEL, primary_key=True)


class ClientProfile(BaseModel):
    user = AutoOneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
