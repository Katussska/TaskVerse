from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)  # use the custom form
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()  # use the custom form
    return render(request, 'user_register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    next_page = '/projects/'
    form_class = LoginForm
