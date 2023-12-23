from django.shortcuts import render
from authentication_app1 import forms

"""1. **Créer une vue de connexion :** Implémentez une vue Django 
qui permet aux utilisateurs de se connecter 
en utilisant leur nom d'utilisateur (ou adresse e-mail) 
et leur mot de passe.
"""
def connect(request):
    return render(request, 'authentication_app1/connect.html')

def deconnect(request):
    formulaire_connexion = Form_Connect()
    return render(request, 'authentication_app1/deconnect.html')

