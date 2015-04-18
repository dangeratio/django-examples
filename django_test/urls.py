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

    # user auth urls
    (r'^accounts/login/$', 'django_test.views.login'),
    (r'^accounts/auth/$', 'django_test.views.auth_view'),
    (r'^accounts/logout/$', 'django_test.views.logout'),
    (r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    (r'^accounts/invalid_login/$', 'django_test.views.invalid_login'),

    # registration urls
    (r'^accounts/register/$', 'django_test.views.register_user'),
    (r'^accounts/register_success/$', 'django_test.views.register_success'),


)