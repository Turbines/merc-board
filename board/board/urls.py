from __future__ import unicode_literals
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/', 'accounts.views.register', name='register'),

    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', 'accounts.views.home', name='home')
)
