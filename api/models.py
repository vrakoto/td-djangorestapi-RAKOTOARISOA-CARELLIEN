from django.db import models

class Chercheur(models.Model):
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class ProjetDeRecherche(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin_prevue = models.DateField()
    chef_de_projet = models.ForeignKey(Chercheur, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre

class Publication(models.Model):
    titre = models.CharField(max_length=100)
    resume = models.TextField()
    projet_associe = models.ForeignKey(ProjetDeRecherche, on_delete=models.CASCADE)
    date_publication = models.DateField()

    def __str__(self):
        return self.titre