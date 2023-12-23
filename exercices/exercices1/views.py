from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from . import forms , models
from django.http import HttpResponse


"""Création d'une Vue de Connexion Simple :

Créez une vue de base qui affiche un formulaire 
de connexion avec 
des champs pour le nom d'utilisateur et le mot de passe."""

@login_required
def home(request):
    return render(request, 'exercices1/home.html')

def LoginView(request): #connect_user: je renommé cette vue en LoginView
    message = ''
    form = forms.Formulaire_Connexion()
    if request.method == 'POST':
        form = forms.Formulaire_Connexion(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #message = f"vous étes connecté { user.username }"
                return redirect('home')
            else:
                message = "Identifiants Invalides !"
    else:
        form = forms.Formulaire_Connexion()

    return render(request, 'exercices1/gabarit_connexion.html', {'form':form, 'message':message})

def deconnect_user(request):
    logout(request)
    return render(request, 'exercices1/deconnect_user.html')

def inscriver_utilisateur(request):
    form = forms.Form_Inscription()
    user = models.UserManagement()
    if request.method == 'POST':
        form = forms.Form_Inscription(request.POST)
        if form.is_valid():
            user = models.UserManagement(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            email = form.cleaned_data['email']
            )
            user.save()
            #return redirect('home')
            contenu = f"user saved succefully { user.username } - { user.password } -  { user.email }"
            return HttpResponse(contenu) 

        else:
            form = forms.Form_Inscription(request.POST)

    else:
        form = forms.Form_Inscription()      

    return render(request, 'exercices1/inscription.html', context={'form':form, 'user':user})



