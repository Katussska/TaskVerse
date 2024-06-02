from django.urls import path

from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('create/', views.ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('<int:project_id>/team/', views.team_members, name='team_members'),
    path('<int:project_id>/team/remove/<int:user_id>', views.remove_team_member, name='remove_team_member'),
    path('<int:pk>/update/', views.ProjectUpdateView.as_view(), name='update_project'),
]
