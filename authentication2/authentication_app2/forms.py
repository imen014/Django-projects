# authentication/forms.py
#2eme etape aprés creation de modele user 
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')