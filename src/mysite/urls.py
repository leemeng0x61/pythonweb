from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from d.views import archive_d

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^d/$', archive_d),
)
