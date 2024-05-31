from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from ui.ui import TextInput, TextArea
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


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    first_name = forms.CharField(label='First name', widget=TextInput(attrs={
        'name': 'first_name',
        'placeholder': 'Michal'
    }))
    last_name = forms.CharField(label='Last name', widget=TextInput(attrs={
        'name': 'last_name',
        'placeholder': 'Kratky'
    }))
    email = forms.CharField(label='Email', widget=TextInput(attrs={
        'type': 'email',
        'name': 'email',
    }))
    bio = forms.CharField(label='Bio', widget=TextArea)

    class Meta:
        model = User
        fields = [
            'profile_picture',
            'first_name',
            'last_name',
            'email',
            'bio',
        ]
