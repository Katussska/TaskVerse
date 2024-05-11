from django.shortcuts import render
from .models import Project


def project_list(request):
    # founded_projects = Project.objects.filter(founder=request.user)
    # team_projects = Project.objects.filter(team=request.user)
    #
    # projects = founded_projects | team_projects

    # return render(request, 'project_list.html', {'projects': projects})
    return render(request, 'project_list.html')
