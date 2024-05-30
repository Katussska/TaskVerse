from django.core.paginator import Paginator
from django.shortcuts import render

from tasks.models import Task


def task_list(request):
    # TODO:
    # tasks = Task.objects.filter(Q(project__founder=request.user) | Q(project__team=request.user))
    task_list = Task.objects.all()
    paginator = Paginator(task_list, 10)

    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    return render(request, 'task_list.html', {'tasks': tasks})
