from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from postings.views import PostingCreateView

urlpatterns = patterns('',
                       url(r'create/$',
                           login_required(PostingCreateView.as_view()),
        name='posting-create'))