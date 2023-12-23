from books_management_app.models import Books
from django import forms

class Formulaire_ajout_livres(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'

"""7. **Mise à jour des données :**
   Ajoutez une fonctionnalité de mise à jour pour permettre 
   aux utilisateurs de modifier 
les informations d'un livre existant. Créez un nouveau formulaire 
modelform pour la mise à jour.
"""

class Formulaire_update_data(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'