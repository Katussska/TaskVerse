from django import forms
from django.contrib.auth import get_user_model

from ui.ui import TextInput, TextArea, SelectMultiple
from .models import Project

User = get_user_model()


class ProjectForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=TextInput(attrs={
        'name': 'name',
    }))
    description = forms.CharField(label='Description', widget=TextArea)

    team_members = forms.ModelMultipleChoiceField(widget=SelectMultiple,
                                                  required=False,
                                                  queryset=User.objects.none())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ProjectForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['team_members'].queryset = User.objects.exclude(id=self.user.id)

    class Meta:
        model = Project
        fields = ['name', 'description']
