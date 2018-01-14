from django import forms
from blog.models import *


class PostMessageForm(forms.ModelForm):
    post_title = forms.CharField(max_length=20, required=False,
                                 widget=forms.TextInput(attrs={'placeholder': 'Заголовок'})
                                 )
    post_text = forms.CharField(max_length=20, required=False,
                                widget=forms.TextInput(attrs={'placeholder': 'Текст поста'})
                                )

    class Meta:
        model = PostMessage
        fields = ('post_title', 'post_text')