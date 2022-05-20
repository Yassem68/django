from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class ResauxForm(ModelForm):
    class Meta :
        model = models.Reseaux
        fields = ('nom_rs', 'createur','date_sortie', 'utilite', 'lieu_creation', 'nb_utilisateurs', 'description')
        labels = {
            'nom_rs' : _('Nom du réseau social'),
            'createur' : _('Nom du créateur'),
            'date_sortie' : _('Date de sortie '),
            'utilite' : _('Utilité du réseau social'),
            'lieu_creation' : _('Lieu de création'),
            'nb_utilisateurs' : _('Nombre utilisateurs'),
            'description' : _('Description'),
        }

class CreateurForm(ModelForm):
    class Meta :
        model = models.Createur
        fields = ('nom', 'prenom','nom_rs', 'date_naissance', 'lieu_naissance', 'nationnalite', 'plus')
        labels = {
            'nom' : _('Nom du Créateur'),
            'prenom' : _('Prénom du créateur'),
            'nom_rs' : _('Nom du réseau social créé par le concepteur '),
            'date_naissance' : _('Date de naissance'),
            'lieu_naissance' : _('Lieu de naissance'),
            'nationnalite' : _('Nationnalité'),
            'plus' : _('Autres infos'),
        }