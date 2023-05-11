from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'author', 'img_url', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'img_url': forms.URLInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

    title = forms.CharField(label='Blog Post Title')
    subtitle = forms.CharField(label='Subtitle')
    author = forms.CharField(label='Your Name')
    img_url = forms.URLField(label='Blog Image URL')
    body = forms.CharField(widget=forms.Textarea(), label='Blog Content')
    # submit = forms.SubmitField(label='Submit Post', widget=forms.TextInput(attrs={'class': 'form-control'}))

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']