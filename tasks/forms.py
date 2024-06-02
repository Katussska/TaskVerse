from django import forms

from projects.forms import User
from projects.models import Project
from tasks.models import Task
from ui.ui import TextInput, TextArea, Select


class EditTaskForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=TextInput(attrs={
        'name': 'name',
    }))
    description = forms.CharField(label='Description', widget=TextArea)
    project = forms.ModelChoiceField(
        widget=Select,
        queryset=Project.objects.all()
    )
    assigned_to = forms.ModelChoiceField(
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
            self.fields['assigned_to'].queryset = User.objects.filter(projects__in=[self.instance.project])

    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'project',
            'assigned_to',
            'priority',
            'status'
        ]


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'assigned_to',
            'priority',
            'status'
        ]

    name = forms.CharField(label='Name', widget=TextInput(attrs={
        'name': 'name',
        'placeholder': 'Task title',
    }))
    description = forms.CharField(label='Description', widget=TextArea(attrs={
        'placeholder': 'Task description'
    }))
    assigned_to = forms.ModelChoiceField(
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
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].label = 'Assignee'
