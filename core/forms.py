from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = '__all__'
