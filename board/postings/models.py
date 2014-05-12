from django.db import models
from taggit.managers import TaggableManager

from board.models import BaseModel, ClientProfile


class Posting(BaseModel):
    poster = models.ForeignKey(ClientProfile, related_name="postings")

    title = models.CharField(max_length=200)
    description = models.TextField()
    start = models.DateField()
    remote = models.BooleanField(default=True)
    public = models.BooleanField(default=True)

    tags = TaggableManager()

