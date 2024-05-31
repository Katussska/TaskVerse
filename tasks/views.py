from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from tasks.forms import TaskForm
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
        context['new_url'] = f'/projects/{project_id}/tasks/new'
        return context


class TaskEditView(UpdateView):
    model = Task
    template_name = 'task_form.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy('task_detail', kwargs={
            'projectId': self.object.project.id,
            'pk': self.object.id
        })
