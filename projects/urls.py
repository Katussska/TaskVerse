from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/', views.project_list, name='project_list'),
    # path('<int:project_id>/', views.project_detail, name='project_detail'),
    # path('create/', views.create_project, name='create_project'),
    # path('<int:project_id>/update/', views.update_project, name='update_project'),
]