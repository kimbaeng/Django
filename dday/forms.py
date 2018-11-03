from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'msg')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'text', 'start', 'finish', 'status')
