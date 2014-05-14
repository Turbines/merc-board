from django import forms
from taggit.managers import TaggableManager


class FeedFilterForm(forms.Form):
    remote = forms.BooleanField()
    tags = TaggableManager()