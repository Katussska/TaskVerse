from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ui.text_input import TextInput
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


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
