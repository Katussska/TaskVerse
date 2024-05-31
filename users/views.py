from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm, UserProfileForm


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


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print('Form is not valid')
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'user_profile.html', {'form': form})
