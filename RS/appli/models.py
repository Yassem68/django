from django.db import models

# Create your models here.

class Reseaux (models.Model):
    nom_rs = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)
    date_sortie = models.DateField(blank= True , null= True)
    utilite = models.CharField(max_length=100)
    lieu_creation = models.CharField(max_length=100)
    nb_utilisateurs = models.IntegerField (blank= False)
    description = models.TextField(null= True, blank= True)


    def __str__(self):
        return self.nom_rs

    def dico(self):
        return {"nom":self.nom_rs, "createur":self.createur, "date_sortie":self.date_sortie, "utilite":self.utilite, "lieu_creation":self.lieu_creation, "nb_utilisateurs":self.nb_utilisateurs, "description":self.description}


class Createur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nom_rs = models.CharField(max_length=100)
    date_naissance = models.DateField(blank = True, null = True)
    lieu_naissance = models.CharField(max_length=100)
    nationnalite = models.CharField(max_length=100)
    plus = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.nom

    def dico2(self):
        return {"nom":self.nom, "artiste":self.prenom, "date":self.nom_rs, "date_naissance":self.date_naissance, "lieu_naissance":self.lieu_naissance, "nationnalite":self.nationnalite, "plus":self.plus}