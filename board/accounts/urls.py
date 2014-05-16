from __future__ import unicode_literals
from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from accounts import views

urlpatterns = patterns('',
                       url(r"", include('django.contrib.auth.urls')),
                       url(r'^register/$', 'accounts.views.register', name='register'),
                       url(r'^edit/$',
                           login_required(views.ProfileUpdateView.as_view()),
                           name='edit-profile'),
                       url(r'^profile/(?P<pk>\d+)/$',
                           login_required(views.ProfileDetailView.as_view()),
                           name='profile'))