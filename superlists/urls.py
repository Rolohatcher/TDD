from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', # Examples:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^favicon.ico$', 'lists.views.favicon', name='favicon')
)
