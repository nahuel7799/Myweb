from django import forms
from .models import Blog, Page

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'
