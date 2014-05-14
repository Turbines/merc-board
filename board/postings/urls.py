from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from postings.views import PostingCreateView, posting_feed, PostingDetailView, \
    PostingUpdateView

urlpatterns = patterns('',
                       url(r'create/$',
                           login_required(PostingCreateView.as_view()),
                           name='posting-create'),
                       url(r'feed/$',
                           posting_feed,
                           name='posting-feed'),
                       url(r'detail/(?P<pk>\d+)/$',
                           login_required(PostingDetailView.as_view()),
                           name="posting-detail"),
                       url(r'update/(?P<pk>\d+)/$',
                           login_required(PostingUpdateView.as_view()),
                           name='posting-update'))