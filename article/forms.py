from django import forms
from models import Article


class ArticleForm(forms.ModelForm):

    # used to define anything that isn't a form field
    class Meta:
        model = Article
        # needed in django 1.8 and up (not from the tutorial, but necessary to make it work in new django)
        fields = '__all__'
        # alternately you can specify fields
        fields = ('title', 'body', 'pub_date', 'thumbnail')