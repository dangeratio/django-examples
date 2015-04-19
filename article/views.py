"""
### old code from first couple tutorials
###

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
from django.http import HttpResponse
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

import logging

logger = logging.getLogger(__name__)


def root(request):
    return HttpResponseRedirect('/articles/all')


def articles(request):

    language = "en-us"
    session_language = "en-us"

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))

    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles.html', args)


def article(request, article_id=1):
    return render_to_response('article.html',
        {'article': Article.objects.get(id=article_id) })


def language(request, language='en-us'):
    response = HttpResponse('setting language to %s' % language)

    # set cookie var
    response.set_cookie('lang', language)

    # set session var
    request.session['lang'] = language

    return response


def create(request):

    if request.POST:
        # if returning to itself, verses the first time arriving
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        # create a blank form for the user to submit
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_article.html', args)


def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        # count = a.likes
        # count += 1
        # a.likes = count
        a.likes += 1
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)


def search_titles(request):

    if request.method == "POST":
        search_text = request.POST['search_text']
        if search_text is not None and search_text != u"":
            articles = Article.objects.filter(title__contains=search_text)
        else:
            articles = None
    else:
        articles = None

    return render_to_response('ajax_search.html', {'articles': articles})
