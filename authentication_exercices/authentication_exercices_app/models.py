from django.db import models

from django.contrib.auth.models import AbstractBaseUser

class Users(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=10)

    USERNAME_FIELD = 'username'

"""Création d'un modèle utilisateur personnalisé :

Créez un modèle utilisateur personnalisé en utilisant la classe AbstractBaseUser 
de Django.
Ajoutez simplement les champs de base tels que le nom d'utilisateur et le mot de passe.""" 
