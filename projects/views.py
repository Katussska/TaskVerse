from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django.views.generic import DetailView

from tasks.models import Task
from users.models import User
from .forms import ProjectForm, AddTeamMemberForm
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

    def get_form_kwargs(self):
        kwargs = super(CreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.founder = self.request.user
        response = super().form_valid(form)
        form.instance.team.add(*form.cleaned_data['team_members'])
        return response


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.object.id
        context['new_url'] = f'/projects/{project_id}/tasks/create'
        context['team_url'] = f'/projects/{project_id}/team/'
        tasks = Task.objects.filter(project_id=project_id)

        paginator = Paginator(tasks, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['tasks'] = page_obj
        return context


def team_members(request, project_id):
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        form = AddTeamMemberForm(request.POST, project=project)
        if form.is_valid():
            user = form.cleaned_data['user']
            project.team.add(user)
            return redirect('team_members', project_id=project.id)
    else:
        form = AddTeamMemberForm(project=project)
    return render(request, 'project_team.html', {'project': project, 'form': form})


@require_POST
def remove_team_member(request, user_id, project_id):
    project = Project.objects.get(id=project_id)
    user = User.objects.get(id=user_id)
    project.team.remove(user)
    return redirect('team_members', project_id=project.id)
