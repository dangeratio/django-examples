"""
# base import
from django.shortcuts import render
from django.http import HttpResponse

# templates
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView


# Create your views here.

def hello(request):
    name = "Andy"
    html = "<html><body>Hi %s, this seams to have worked!</body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Andy"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = "Andy"
    return render_to_response('hello.html', {'name': name})

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Andy'
        return context
"""

from django.shortcuts import render_to_response
from article.models import Article


def articles(request):
    return render_to_response('articles.html',
        {'articles': Article.objects.all() })


def article(request, article_id=1):
    return render_to_response('article.html',
        {'article': Article.objects.get(id=article_id) })

