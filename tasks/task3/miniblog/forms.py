from .models import PostComment
from django import forms


class CommentsForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['body']
