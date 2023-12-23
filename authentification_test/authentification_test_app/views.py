from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from authentification_test_app.models import CustomUser


def create_user(request):
    user = CustomUser.objects.create(username="sami",password="P@ssw0rd0147", date_of_birth = '2023-10-06')
    return render(request, 'authentification_test_app/login.html', {'user':user})


def signup(request):
    if request.method == 'POST':
        pass

    return render(request, 'authentification_test_app/signup.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('profil')
            else:
                pass

        else:
            form = LoginForm()
    return render(request, 'authentification_test_app/login.html', {'form':form})

