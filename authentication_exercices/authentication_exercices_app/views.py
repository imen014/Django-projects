from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from authentication_exercices_app.models import Users

from .forms import FormulaireLogin

def create_user(request):
    user = Users.objects.create(username="ali")
    user.set_password("123456789")
    user.save()
    return render(request, 'authentication_exercices_app/create_user.html', {'user':user})

def get_user(request, id):
    user = Users.objects.get(id=id)
    return render(request, 'authentication_exercices_app/get_user.html', {'user':user})

def formulaire_de_connexion(request):
    form = FormulaireLogin()
    if request.method == 'POST':
        form = FormulaireLogin(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('get_user', id = user.id)
            


    else:
        form = FormulaireLogin()

    return render(request, 'authentication_exercices_app/login.html', {'user':user})
