from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError


"""1. **Champs de caractères** :
   - Créez un modèle pour représenter des produits avec des champs 
   tels que le nom (CharField),
 la description (TextField), et le code SKU (CharField unique).
   - Ajoutez un modèle pour les commentaires de produits avec 
   un champ de texte long (TextField) 
pour les commentaires."""

class Produit(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    code_SKU = models.CharField(unique=True, max_length=10)

class Commentaires_Produit(models.Model):
    texte = models.TextField()

"""2. **Champs numériques** :
   - Créez un modèle pour représenter des transactions financières 
   avec des champs tels
 que le montant (DecimalField) et le numéro de compte (IntegerField).
   - Ajoutez un modèle pour les étudiants avec un champ pour leur 
   moyenne (FloatField).
"""

class Transactions_financieres(models.Model):
    montant = models.DecimalField(max_digits=4, decimal_places=2)
    numero_compte = models.IntegerField()

class Etudiant(models.Model):
    moyenne = models.FloatField()

"""3. **Champs de date et d'heure** :
   - Concevez un modèle pour représenter des événements avec des champs
     de date (DateField) 
et d'heure (TimeField).
   - Ajoutez un modèle pour les tâches à faire avec un champ pour 
   la date d'échéance (DateField).
"""
class My_Events(models.Model):
    date = models.DateField()
    heure = models.TimeField()

class Taches_afaire(models.Model):
    date_echeance = models.DateField()

"""4. **Champs booléens** :
   - Créez un modèle pour les utilisateurs avec un champ booléen (BooleanField) pour activer 
ou désactiver leur compte.
   - Ajoutez un modèle pour les articles de blog avec un champ booléen pour indiquer s'ils sont 
publiés ou en brouillon."""

class Utilisateurs(models.Model):
    state_account = models.BooleanField()

class Articles_Blog(models.Model):
    publiee = models.BooleanField()

"""5. **Champs de clé étrangère** :
   - Concevez un modèle pour les commandes de produits avec une clé étrangère vers le modèle 
de produit.
   - Ajoutez un modèle pour les commentaires de blog avec une clé étrangère vers le modèle d'article
 de blog."""

class Produit(models.Model):
    quantite_stock = models.IntegerField(default=0)
    fournisseur = models.CharField(max_length=20, null=True, blank=True)

class Commandes_Produit(models.Model):
    id_produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True, blank=True)
    nom_commandes = models.CharField(max_length=20)


"""6. **Champs de fichier** :
   - Créez un modèle pour les profils d'utilisateur avec un champ pour télécharger une photo
 de profil (ImageField).
   - Ajoutez un modèle pour les téléchargements de fichiers avec un champ pour télécharger
 des fichiers (FileField)."""

class Profils_Utilisateurs(models.Model):
    photo_de_profil = models.ImageField()


class telecharger_fichiers(models.Model):
    fichier = models.FileField()


"""7. **Champs de liste de choix** :
   - Concevez un modèle pour les quiz avec un champ de liste de choix 
   (CharField avec choix) 
pour les types de question (par exemple, choix multiples, vrai/faux).
   - Ajoutez un modèle pour les produits avec un champ de liste 
   de choix pour les catégories 
de produits (par exemple, électronique, vêtements, alimentation)."""

class Quiz(models.Model):

    liste_choix = (
        ('CHM','CHOIX MULTIPLES'),
        ('CHO', 'CHOIX UNIQUES')
    )
    choix = models.CharField(choices=liste_choix,max_length=60)

class Produits(models.Model):
    categories = (
        ('EL','ELECTRONIQUE'),
        ('VM', 'VETEMENTS'),
        ('AL','ALIMENTATION')
    )

    choix_produit = models.CharField(choices=categories, max_length=50)

"""8. **Champs géospatiaux** :
   - Créez un modèle pour les lieux avec des champs géospatiaux 
   (PointField ou PolygonField) 
pour les coordonnées géographiques.
   - Ajoutez un modèle pour les itinéraires de voyage avec un champ
     géospatial pour le tracé
 de l'itinéraire."""

"""9. **Champs d'URL et d'e-mail** :
   - Concevez un modèle pour les liens avec un champ pour les URL (URLField).
   - Ajoutez un modèle pour les contacts avec un champ pour les adresses e-mail (EmailField).
"""

class liens(models.Model):
    url = models.URLField()
   
class Contact(models.Model):
    email = models.EmailField()


"""10. **Champs de relation many-to-many** :
    - Créez un modèle pour les groupes d'utilisateurs avec une relation many-to-many vers le modèle
 d'utilisateur.
    - Ajoutez un modèle pour les événements avec une relation many-to-many vers le modèle d'invités.
"""

class Users(models.Model):
    nom = models.CharField(max_length=20)

class Users_Groupes(models.Model):
    titre = models.CharField(max_length=50)
    relation = models.ManyToManyField(Users)

class Invitees(models.Model):
    nom = models.CharField(max_length=50)

class Events(models.Model):
    titre = models.CharField(max_length=50)
    membres = models.ManyToManyField(Invitees)


"""**Exercice 11 : Modèle `Client`**
1. Créez un modèle Django nommé `Client` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 2 caractères.
   - `adresse` (CharField) : Doit avoir au moins 5 caractères.
   - `code_postal` (CharField) : Doit avoir exactement 5 caractères 
   numériques.
"""

def validate_code_postal(value):
    if not value.isdigit() or len(value) != 5:
        raise ValidationError("Le code postal doit avoir exactement 5 caractéres !")



class Client(models.Model):
    nom = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    adresse = models.CharField(max_length=200, validators=[MinLengthValidator(5)])
    code_postal = models.CharField(max_length=100, validators=[validate_code_postal])

"""**Exercice 12 : Modèle `Projet`**
1. Créez un modèle Django nommé `Projet` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 3 caractères.
   - `date_debut` (DateField) : Doit être une date dans le passé.
   - `date_fin` (DateField) : Doit être une date dans le futur.
   - `budget` (DecimalField) : Doit être un nombre décimal positif."""

class Projet(models.Model):
    nom = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    date_debut = models.DateField()
    date_fin = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=7)

    def clean(self):
        if self.date_debut and self.date_fin:
            if self.date_debut >= self.date_fin:
                raise ValidationError("la date de debut doit etre antérieure à la date fin")
            
            if self.budget <=0:
                raise ValidationError("le budget doit etre superieur à zero !")
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super(Projet, self).save(*args, **kwargs)

"""**Exercice 13 : Modèle `Produit` avec ImageField**
1. Créez un modèle Django nommé `ProduitAvecImage` avec les champs 
suivants :
   - `nom` (CharField) : Doit avoir au moins 5 caractères.
   - `description` (TextField) : Doit avoir au moins 10 caractères.
   - `image` (ImageField) : Permettez aux utilisateurs de télécharger 
   une image du produit.
"""

class ProduitAvecImage(models.Model):
    nom = models.CharField(max_length=20, validators=[MinLengthValidator(5)])
    description = models.TextField(validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to='images')

"""**Exercice 14 : Modèle `Employé` avec DateField et EmailField**
1. Créez un modèle Django nommé `Employé` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 2 caractères.
   - `date_embauche` (DateField) : Doit être une date dans le passé.
   - `email` (EmailField) : Doit être une adresse e-mail valide.
"""

class Employee(models.Model):
    nom = models.CharField(max_length=20, validators=[MinLengthValidator(2)])
    date_embauche = models.DateField()
    email = models.EmailField()

    def validation(value):
        if this.date_embauche >= '2023-09-18':
            raise ValueError("la date d'embauche doit etre anterieure")
        
        if not self.email:
            raise ValueError("verifier l'email")
        
    def save(self,*args, **kwargs):
        self.full_clean()
        super(Employee, self).save(*args, **kwargs)


"""**Exercice 15 : Modèle `Commande` avec ManyToManyField**
1. Créez un modèle Django nommé `Commande` avec un champ `produits` qui est une relation ManyToMany 
vers le modèle `Produit`. Une commande peut contenir plusieurs produits, et un produit peut être inclus 
dans plusieurs commandes.
"""

class Commande(models.Model):
    produits = models.ManyToManyField(Produit)

"""**Exercice 17 : Modèle `Cours` avec BooleanField**
1. Créez un modèle Django nommé `Cours` avec les champs suivants :
   - `titre` (CharField) : Doit avoir au moins 5 caractères.
   - `actif` (BooleanField) : Indique si le cours est actif ou non."""

class Cours(models.Model):
    titre = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    actif = models.BooleanField(default=True)
        
"""**Exercice 18 : Modèle `Événement` avec TimeField**
1. Créez un modèle Django nommé `Événement` avec les champs suivants :
   - `nom` (CharField) : Doit avoir au moins 3 caractères.
   - `heure_debut` (TimeField) : Doit spécifier l'heure de début de l'événement.
"""

class Evenement(models.Model):
    nom = models.CharField(max_length=15, validators=[MinLengthValidator(3)])
    heure_debut = models.TimeField()

"""**Exercice 19 : Modèle `Musique` avec FileField**
1. Créez un modèle Django nommé `Musique` avec les champs suivants :
   - `titre` (CharField) : Doit avoir au moins 3 caractères.
   - `fichier_audio` (FileField) : Permettez aux utilisateurs 
   de télécharger un fichier audio.
"""

class Musique(models.Model):
    titre = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    fichier_audio = models.FileField()

"""**Exercice 20 : Modèle `Destination` avec ChoiceField**
1. Créez un modèle Django nommé `Destination` avec les champs 
suivants :
   - `nom` (CharField) : Doit avoir au moins 3 caractères.
   - `type` (CharField avec choix) : Les choix possibles sont "Plage",
     "Montagne", "Ville".
"""

class Destination(models.Model):
    choix_type_ville = (
        ('PL','Plage'),
        ('Mng', 'Montagne'),
        ('VL','Ville')
    )

    nom = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    type_ville = models.CharField(max_length=50, choices=choix_type_ville)