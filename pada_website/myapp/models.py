from django.db import models

class Rue(models.Model):
    nom_rue = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    x = models.FloatField()
    y = models.FloatField()
    h = models.IntegerField()
    description = models.TextField()
    # url = models.CharField(max_length=200) 

    def __str__(self):
        return f"{self.nom_rue} - {self.quartier}"


 