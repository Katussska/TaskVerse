from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from projects.models import Project
from tasks.forms import EditTaskForm, CreateTaskForm
from tasks.models import Task


def task_list(request):
    # TODO:
    # tasks = Task.objects.filter(Q(project__founder=request.user) | Q(project__team=request.user))
    task_list = Task.objects.all()
    paginator = Paginator(task_list, 10)

    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(request, 'task_list.html', {'tasks': tasks})


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_id = self.object.project.id
        task_id = self.object.id
        context['edit_url'] = f'/projects/{project_id}/tasks/{task_id}/edit'
        context['new_url'] = f'/projects/{project_id}/tasks/create'
        return context


def create_task(request, projectId):
    project = get_object_or_404(Project, id=projectId)
    team_members = project.team.all()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        form.fields['assignee'].queryset = team_members
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_detail',
                            projectId=project.id,
                            pk=task.id)
        else:
            print('Form is not valid')
            print(form.errors)
    else:
        form = CreateTaskForm()

    form.fields['assignee'].queryset = team_members

    return render(request, 'task_form.html', {'form': form, 'project': project})


class TaskEditView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    form_class = EditTaskForm

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={
            'projectId': self.object.project.id,
            'pk': self.object.id
        })
