from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Project

User = get_user_model()


class ProjectForm(forms.ModelForm):
    team_usernames = forms.CharField(required=False)

    class Meta:
        model = Project
        fields = ['name', 'description']

    def clean_team_usernames(self):
        usernames = self.cleaned_data.get('team_usernames')

        if not usernames:  # if usernames is empty, return an empty list
            return []

        users = []

        for username in usernames.split(','):
            try:
                user = User._default_manager.get(username=username.strip())
                users.append(user)
            except User.DoesNotExist:
                raise ValidationError(f'User with username {username} does not exist.')
            
        return users
