from django.forms import ModelForm
from .models import Produit,Fournisseur,Commande,Categorie
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms.models import inlineformset_factory
from magasin import models



class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__" 
        # pour tous les champs de la table
        # fields=['libelle','description'] # pour quelques champs
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
   
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"
        widgets = {
            'produits': forms.CheckboxSelectMultiple()
        }


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"




