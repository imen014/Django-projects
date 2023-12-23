from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class Formulaire_Connexion(AuthenticationForm):
    username = forms.CharField(max_length=50, label="username")
    password = forms.CharField(max_length=15, widget=forms.PasswordInput, label="password")
    email = forms.EmailField(label="email")

class Form_Inscription(UserCreationForm):
    class Meta(UserCreationForm.Meta):

        model = get_user_model()
        fields = ['username', 'email', 'password']