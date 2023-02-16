from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'name': 'إسمك',
            'email':'بريدك الالكتروني',
            'body': 'تعليقك',
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control"}),
        }