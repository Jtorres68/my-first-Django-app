from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    #tells which model should be used to create this form
    class Meta:
        model = Post
        fields = ('address', 'description',)