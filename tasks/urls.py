from django.urls import path

from . import views

urlpatterns = [
    path('<int:projectId>/tasks/<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:projectId>/tasks/<int:pk>/edit', views.TaskEditView.as_view(), name='task_edit'),
]
