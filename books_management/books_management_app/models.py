from django.db import models

"""1. **Créer un modèle de base :**
   Commencez par créer un modèle Django simple, comme un modèle
     représentant des livres avec des champs 
tels que le titre, l'auteur et la date de publication.
"""

class Books(models.Model):
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    date_publication = models.DateField()