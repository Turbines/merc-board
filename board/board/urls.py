from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),

    url('', include('social.apps.django_app.urls', namespace='social')),

    url(r'^$', 'board.views.home', name='home')
)
