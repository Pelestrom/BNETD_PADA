from django.db import models

class Voie(models.Model):
    id = models.AutoField(primary_key=True)
    nom_voies = models.CharField(max_length=255)
    quartier = models.CharField(max_length=255)
    X = models.CharField(max_length=255)
    Y = models.CharField(max_length=255)
    qr_code = models.TextField()
    description = models.CharField(max_length=255)
    entites_territoriales_2 = models.TextField()
    typologie = models.TextField()  # Nouvelle colonne ajoutée

    class Meta:
        db_table = 'panneautage'
        managed = False

    def __str__(self):
        return f"{self.nom_voies} - {self.quartier}"