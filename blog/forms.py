from django import forms
from django.contrib.auth.models import User
from blog.models import *


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password')


class PostMessageForm(forms.ModelForm):

    class Meta:
        model = PostMessage
        exclude = ('post_user', 'post_likes', 'post_date')


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(max_length=255, required=True)

    class Meta:
        model = Comment
        exclude = ('comment_user', 'comment_date', 'comment_post')
