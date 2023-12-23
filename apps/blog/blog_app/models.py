from django.db import models

class Blog(models.Model):
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=50)
    date_pub = models.DateField()
    commentaire = models.TextField()


