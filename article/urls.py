from django.conf.urls import patterns, include, url
# from article.api import ArticleResource
# from tastypie.api import Api

# article_resource = ArticleResource()
# v1_api = Api()
# v1_api.register(ArticleResource())

urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),
    url(r'^create/$', 'article.views.create'),
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),
    url(r'^search/$', 'article.views.search_titles'),

    # APIs
    # url(r'^api/$', include(article_resource.urls)),
    # url(r'^api/', include(v1_api.urls)),

)

