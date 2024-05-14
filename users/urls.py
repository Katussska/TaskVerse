from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

from .views import CustomLoginView, register, LogoutView

urlpatterns = [
    path('', RedirectView.as_view(url='login/'), name='redirect-to-login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('profile/', auth_views.LoginView.as_view(template_name='user_profile.html'), name='profile'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
