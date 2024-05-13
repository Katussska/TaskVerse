from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProjectForm
from .models import Project


def project_list(request):
    founded_projects = Project.objects.filter(founder=request.user)
    team_projects = Project.objects.filter(team=request.user)

    projects = founded_projects | team_projects

    return render(request, 'project_list.html', {'projects': projects})


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_create.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        form.instance.founder = self.request.user
        response = super().form_valid(form)
        self.object.team.set(form.cleaned_data['team_usernames'])
        return response
