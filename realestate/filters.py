from .models import Post
import django_filters
from django import forms
from django.forms import CheckboxSelectMultiple

class PostFilter(django_filters.FilterSet):
    #state = django_filters.ModelMultipleChoiceFilter(queryset = Post.objects.all(), widget=CheckboxSelectMultiple)
    
    class Meta:
        model = Post
        fields = ('seller',)