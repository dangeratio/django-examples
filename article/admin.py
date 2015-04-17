from django.contrib import admin
from article.models import Article

# makes articles aware of admin class

admin.site.register(Article)

