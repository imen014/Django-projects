from django.db import models
from django.contrib.auth.models import AbstractUser


"""Création d'un Modèle Utilisateur Simple :

Créez un modèle utilisateur simple avec des champs tels que 
nom d'utilisateur,
 mot de passe et adresse e-mail."""

class UserManagement(AbstractUser):
    username = models.CharField(max_length=50, unique=True, verbose_name="nom utilisateur")
    email = models.EmailField()

