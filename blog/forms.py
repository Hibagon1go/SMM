from django import forms
from .models import Blog

from django_summernote.widgets import SummernoteWidget
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text')
        widgets = {
                'text': SummernoteWidget(),
        }