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
            "name": forms.TextInput(attrs={"class": "block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"}),
            'email': forms.EmailInput(attrs={"class": "block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"}),
            'body': forms.Textarea(attrs={"class": "block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"}),
        }