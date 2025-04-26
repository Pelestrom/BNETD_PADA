from django.db import models

class Voie(models.Model):
    id = models.AutoField(primary_key=True)
    nom_voies = models.CharField(max_length=255)  # character varying
    quartier = models.CharField(max_length=255)
    X = models.CharField(max_length=255)  # character varying
    Y = models.CharField(max_length=255)  # character varying
    qr_code = models.TextField()
    description = models.CharField(max_length=255)  # character varying
    entites_territoriales_2 = models.TextField()

    class Meta:
        db_table = 'panneautage'  # Remplace par le nom réel de ta table
        managed = False  # Empêche Django de gérer la création/suppression de la table

    def __str__(self):
        return f"{self.nom_voies} - {self.quartier}"


