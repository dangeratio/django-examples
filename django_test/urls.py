# default imports

from django.conf.urls import patterns, include, url

# add admin

from django.contrib import admin, admindocs
admin.autodiscover()

'''
from django.conf.urls import include, url

from django.contrib import admin

# custom views

from article.views import HelloTemplate

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'article.views.hello'),
    url(r'^hello_template/$', 'article.views.hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    url(r'^hello_class_view/$', HelloTemplate.as_view()),
]
'''



urlpatterns = patterns('',
    (r'^articles/', include('article.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)