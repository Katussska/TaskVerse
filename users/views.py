from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm  # import the custom form


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)  # use the custom form
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # use the custom form
    return render(request, 'user_register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    next_page = '/projects/'


class LogoutView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
