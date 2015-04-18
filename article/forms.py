from django import forms
from models import Article


class ArticleForm(forms.ModelForm):

    # used to define anything that isn't a form field
    class Meta:
        model = Article