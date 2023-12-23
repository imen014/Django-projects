from django.db import models

"""1. **Créer un modèle de liste de tâches** : Créez un modèle de liste de tâches avec un champ "titre"
 et un champ "terminé" (booléen) pour représenter si la tâche est terminée ou non.
"""

class Liste_Taches(models.Model):
    titre = models.CharField(max_length=20)
    terminee = models.BooleanField(default=False)

"""2. **Modèle de notes** : Concevez un modèle pour stocker des notes. Chaque note peut avoir un titre 
et un contenu."""

class Note(models.Model):
    titre = models.CharField(max_length=50)
    contenu = models.CharField(max_length=200)

"""3. **Modèle de liste de courses** : Créez un modèle pour une liste de courses avec des champs pour
 les articles, les quantités et les prix.
"""

class Liste_Course(models.Model):
    article = models.CharField(max_length=200)
    quantitee = models.IntegerField()
    prix = models.FloatField()

""". **Modèle de livre de bibliothèque** : Créez un modèle pour représenter des livres de bibliothèque
 avec des champs tels que le titre, l'auteur, l'année de publication, etc.
"""

class Books(models.Model):
    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=20)
    annee_publication = models.DateField()

"""5. **Modèle de liste de contacts** : Concevez un modèle pour 
stocker des contacts avec
 des informations de base telles que le nom, le numéro de téléphone
   et l'adresse e-mail.
"""
class Liste_Contacts(models.Model):
    nom = models.CharField(max_length=20)
    numero_telephone = models.CharField(max_length=15)
    adresse_email = models.EmailField()

"""6. **Modèle de recettes de cuisine** : Créez un modèle pour des 
recettes de cuisine comprenant
 des champs pour le nom de la recette, les ingrédients 
 et les instructions.
"""

class Recette_Cuisine(models.Model):
    nom_recette = models.CharField(max_length=30)
    ingredients = models.CharField(max_length=200)
    instruc_cooking = models.CharField(max_length=300)

"""7. **Modèle de commentaires sur un blog** : Si vous avez déjà 
un modèle de blog, ajoutez un modèle 
de commentaires pour permettre aux utilisateurs de commenter 
les articles.
"""

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=20)

class Commentaire_Blog(models.Model):
    id = models.AutoField(primary_key=True)
    Commentaire = models.CharField(max_length=100)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Blog(models.Model):
    bloggueur = models.CharField(max_length=50)
    contenu_blog = models.CharField(max_length=300)
    id_commentaire = models.ForeignKey(Commentaire_Blog,on_delete=models.SET_NULL, blank=True, null=True)

"""8. **Modèle de questionnaire** : Créez un modèle pour stocker 
les réponses d'un questionnaire simple,
 avec des questions et des réponses textuelles.
"""

class Reponse_questionnaire(models.Model):
    question = models.CharField(max_length=50)
    answer = models.CharField(max_length=100)

    
"""9. **Modèle de produit avec une image** : Similaire à l'exercice 
précédent sur les produits,
 mais cette fois-ci, ajoutez un champ pour télécharger une image 
 du produit.
"""

class Produit_Images(models.Model):
    titre = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

"""10. **Modèle de catégorie de produits** : Créez un modèle pour 
catégoriser les produits,
 par exemple, en ayant un modèle de produit et un modèle de catégorie, 
 puis en liant les produits 
à des catégories."""

class Categories_Produits(models.Model):
    id = models.AutoField(primary_key=True)
    categorie = models.CharField(max_length=50)

class Produit(models.Model):
    nom_produit = models.CharField(max_length=50)
    id_categorie = models.ForeignKey(Categories_Produits, on_delete=models.SET_NULL, blank=True, null=True)

"""11. **Modèle de pays et de ville** : Créez un modèle de pays 
et un modèle de ville, en utilisant
 une clé étrangère pour lier les villes à un pays.
"""

class Pays(models.Model):
    nom_pays = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

class Ville(models.Model):
    nom_ville = models.CharField(max_length=50)
    id_pays = models.ForeignKey(Pays, on_delete=models.SET_NULL, null = True, blank=True)
    
    
"""12. **Modèle d'étudiant** : Concevez un modèle pour représenter
 des étudiants avec des champs 
pour le nom, la date de naissance et la moyenne des notes.
"""

class Etudiant(models.Model):
    nom_etudiant = models.CharField(max_length=50)
    date_naissance = models.DateField()
    moyenne_notes = models.FloatField()