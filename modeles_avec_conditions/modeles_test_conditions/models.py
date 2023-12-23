from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


"""**Exercice 1 : Modèle `Person`**
1. Créez un modèle Django nommé `Person` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 2 caractères.
   - `age` (PositiveIntegerField) : Doit être un entier positif.
   - `adresse` (TextField) : Optionnel."""

class Person(models.Model):
    nom = models.CharField(validators=[MinLengthValidator(2)], max_length=20)
    age = models.PositiveBigIntegerField()
    adresse = models.TextField()

"""**Exercice 2 : Modèle `Produit`**
1. Créez un modèle Django nommé `Produit` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 5 caractères.
   - `prix` (DecimalField) : Doit être un nombre décimal positif avec
     deux décimales.
"""

class Produit(models.Model):
    nom = models.CharField(max_length=20)
    prix = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00)
        ]
    )

    """**Exercice 3 : Modèle `Tâche`**
1. Créez un modèle Django nommé `Tâche` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 3 caractères.
   - `date_limite` (DateField) : Doit être une date future.
"""

class Tache(models.Model):
    nom = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    date_time = models.DateField(
        validators=[MinValueValidator("19-09-2023")]
    )

"""**Exercice 4 : Modèle `Étudiant`**
1. Créez un modèle Django nommé `Étudiant` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 2 caractères.
   - `niveau` (CharField avec choix) : Les choix possibles sont "Première année", "Deuxième année" 
et "Troisième année"."""

class Etudiant(models.Model):

    Choix_Niveau = (
        ('premiere_annee' , 'PR'),
        ('deuxieme_annee' , 'DX'),
        ('troisieme_annee' , 'TA')
    )

    nom = models.CharField(validators=[MinLengthValidator(2)], max_length=20)
    niveau = models.CharField(choices=Choix_Niveau, max_length=20)
