from django.shortcuts import render
from books_management_app.models import Books
from books_management_app.forms import Formulaire_ajout_livres
from django.http import HttpResponse
from books_management_app.forms import Formulaire_update_data

"""3. **Afficher le formulaire :**
   Intégrez ce formulaire dans une vue Django et affichez-le 
   dans un modèle HTML. Assurez-vous que 
le formulaire s'affiche correctement sur la page.
"""

def afficher_form(request):
    formulaire = Formulaire_ajout_livres()
    return render(request, 'books_management_app/afficher_formulaire.html', {'formulaire':formulaire})

"""4. **Validation basique :**
   Ajoutez des règles de validation de base, telles que la validation 
   de champ obligatoire (required),
 à votre formulaire. Testez le formulaire en soumettant des données
   incorrectes.
"""

def validation_formulaire(request):
    if request.method == "POST":
        formulaire = Formulaire_ajout_livres(request.POST)
        if formulaire.is_valid():
            contenu = "votre formulaire est valide !"
            return HttpResponse(contenu)
        else:
            contenu = "verifier les données !"
            return HttpResponse(contenu)
        
    else:
        formulaire = Formulaire_ajout_livres()
        return render(request, 'books_management_app/afficher_formulaire.html', {'formulaire':formulaire})

"""5. **Enregistrement de données :**
   Écrivez une vue pour enregistrer les données soumises 
   par le formulaire dans la base de données. 
Assurez-vous que les données sont correctement enregistrées.
"""

def save_books_in_bd(request):
    if request.method == "POST":
        formulaire = Formulaire_ajout_livres(request.POST)
        if formulaire.is_valid():
            formulaire.save()
            contenu = "vos données ont été enregistrées avec succées !"
            return HttpResponse(contenu)
        else:
            contenu = "verifier votre donnée avant enregistrement !"
            return HttpResponse(contenu)
    else:
        formulaire = Formulaire_ajout_livres()
        return render(request, 'books_management_app/afficher_formulaire.html', {'formulaire':formulaire})

"""6. **Liste des données :**
   Créez une vue qui affiche une liste de tous les livres enregistrés 
   dans la base de données.
 Utilisez Django QuerySet pour extraire les données.
"""

def afficher_liste_livres(request):
    data = Books.objects.all()
    return render(request, 'books_management_app/liste_books.html',{'data':data})

"""7. **Mise à jour des données :**
   Ajoutez une fonctionnalité de mise à jour pour permettre 
   aux utilisateurs de modifier 
les informations d'un livre existant. Créez un nouveau formulaire 
modelform pour la mise à jour.
"""

def update_data(request, id):
    data = Books.objects.get(id=id)
    if request.method == "POST":
        formulaire_de_mise_a_jour = Formulaire_update_data(request.POST, instance=data)
        if formulaire_de_mise_a_jour.is_valid():
            formulaire_de_mise_a_jour.save()
            contenu = "update valide !"
            return HttpResponse(contenu)
        else:
            contenu = "verifier les données avant mise à jour"
            return HttpResponse(contenu)
    else:
        formulaire_de_mise_a_jour = Formulaire_update_data(instance=data)
        return render(request, 'books_management_app/formulaire_de_mise_a_jour.html', {'formulaire_de_mise_a_jour':formulaire_de_mise_a_jour})

"""8. **Suppression des données :**
   Permettez aux utilisateurs de supprimer des livres
     de la base de données en ajoutant un bouton 
de suppression à côté de chaque livre dans la liste.
"""  

def supprimer_livres(request, id):
    formulaire_a_supprimer = Books.objects.get(id=id)
    formulaire_a_supprimer.delete()
    return render(request, 'books_management_app/supprimer_formulaire.html', {'formulaire_a_supprimer':formulaire_a_supprimer})
    

