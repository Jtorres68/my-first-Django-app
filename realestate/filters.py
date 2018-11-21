from .models import Post
import django_filters
from django import forms
from django.forms import CheckboxSelectMultiple
from django.db.models import CharField

class PostFilter(django_filters.FilterSet):
    #state = django_filters.ChoiceFilter(choices=Post.objects.filter(seller))
    class Meta:
        model = Post
        fields = ('seller',)
        