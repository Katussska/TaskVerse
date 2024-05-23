from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ui.ui import TextInput
from django import forms

from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=TextInput(attrs={
        'name': 'username',
        'placeholder': 'kacaba'
    }))
    password = forms.CharField(label='Password', widget=TextInput(attrs={
        'type': 'password',
        'name': 'password',
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=TextInput(attrs={
        'name': 'username',
        'placeholder': 'kacaba'
    }))
    email = forms.CharField(label='Email', widget=TextInput(attrs={
        'type': 'email',
        'name': 'email',
    }))
    password1 = forms.CharField(label='Password', widget=TextInput(attrs={
        'type': 'password',
        'name': 'password1',
    }))
    password2 = forms.CharField(label='Confirm password', widget=TextInput(attrs={
        'type': 'password',
        'name': 'password2',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
