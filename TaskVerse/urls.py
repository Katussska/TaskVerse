"""
URL configuration for TaskVerse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from tasks import views as taskViews
from users.views import profile

urlpatterns = [
                  path('__reload__/', include('django_browser_reload.urls')),
                  path('admin/', admin.site.urls),
                  path('', RedirectView.as_view(url='users/login/'), name='redirect-to-login'),
                  path('users/', include('users.urls')),
                  path('projects/', include('projects.urls')),
                  path('projects/', include('tasks.urls')),
                  path('tasks/', taskViews.task_list, name='task_list'),
                  path('profile/', profile, name='profile')
                  # path('comments/', include('comments.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
