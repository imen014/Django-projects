"""Écrivez un script Python dans un fichier nommé read_data.py 
qui récupère et affiche toutes les tâches de la base de données 
en utilisant le modèle "Tâche".
"""
import os
import django
from CRUD_WITH_Console_app.models import Taches

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRUD_WITH_CONSOLE.settings")

django.setup()




taches = Taches.objects.all()
for tache in taches:
    print("nom de taches : ", tache.nom_tache)

