from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user_login.html'
    redirect_authenticated_user = True
    next_page = '/projects/'
