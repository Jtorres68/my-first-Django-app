from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    
    #tells which model should be used to create this form
    class Meta:
        model = Post
        fields = ('address', 'description', 'seller',)
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text',)