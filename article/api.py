# api.py
#
# uses: tastypie, defusedxml
#
#
'''
from article.models import Article
from tastypie.resources import ModelResource
from tastypie.constants import ALL

class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        # filtering = { 'title': ALL }
        filtering = { 'title': "contains" }
'''
