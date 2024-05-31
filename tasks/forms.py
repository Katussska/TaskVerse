from django import forms

from projects.forms import User
from projects.models import Project
from tasks.models import Task
from ui.ui import TextInput, TextArea, Select


class TaskForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=TextInput(attrs={
        'name': 'name',
    }))
    description = forms.CharField(label='Description', widget=TextArea)
    project = forms.ModelChoiceField(
        widget=Select,
        queryset=Project.objects.all()
    )
    assignee = forms.ModelChoiceField(
        widget=Select,
        queryset=User.objects.none(),
        required=False
    )
    priority = forms.TypedChoiceField(
        widget=Select,
        choices=Task.Priority.choices,
        coerce=str
    )
    status = forms.TypedChoiceField(
        widget=Select,
        choices=Task.Status.choices,
        coerce=str,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.project:
            self.fields['assignee'].queryset = User.objects.filter(projects__in=[self.instance.project])

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'project',
            'assignee',
            'priority',
            'status'
        ]
