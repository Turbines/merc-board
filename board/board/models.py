from django.conf import settings
from django.db import models
from taggit.managers import TaggableManager


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MercenaryProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)


class ClientProfile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)


class Posting(BaseModel):
    poster = models.ForeignKey(ClientProfile, related_name="postings")

    title = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateField()
    remote = models.BooleanField(default=True)
    public = models.BooleanField(default=True)

    tags = TaggableManager()


class Endorsement(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)

    endorsed_mercenaries = models.ManyToManyField('MercenaryProfile', related_name='endorsed_mercenaries')
    endorsed_clients = models.ManyToManyField('ClientProfile', related_name='endorsed_clients')