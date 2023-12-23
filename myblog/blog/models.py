from django.db import models

class Article_Blog_bd(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.CharField(max_length=200)
    date_publication = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
