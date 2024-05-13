from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Project


class ProjectForm(forms.ModelForm):
    team_usernames = forms.CharField(required=False)

    class Meta:
        model = Project
        fields = ['name', 'description']

    def clean_team_usernames(self):
        usernames = self.cleaned_data.get('team_usernames')
        users = []
        for username in usernames.split(','):
            try:
                user = User.objects.get(username=username.strip())
                users.append(user)
            except User.DoesNotExist:
                raise ValidationError(f'User with username {username} does not exist.')
        return users
