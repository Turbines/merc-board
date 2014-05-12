from __future__ import unicode_literals
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r"", include('django.contrib.auth.urls')),
                       url(r'^register/$', 'accounts.views.register', name='register'),
                       url(r'^profile/$', 'accounts.views.profile', name='profile'))