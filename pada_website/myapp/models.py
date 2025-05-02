from django.db import models
from django.db import models
from django.conf import settings
import os
from django.db import models

class Voie(models.Model):
    id = models.AutoField(primary_key=True)
    nom_voies = models.CharField(max_length=255)
    quartier = models.CharField(max_length=255)
    X = models.CharField(max_length=255)
    Y = models.CharField(max_length=255)
    qr_code = models.TextField(unique=True)
    description = models.CharField(max_length=255)
    entites_territoriales_2 = models.TextField()
    photo_personnalite = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'panneautage'
        managed = False

    def __str__(self):
        return f"{self.nom_voies} - {self.quartier}"
    
    @property
    def has_personnalite_photo(self):
        """Vérifie si une photo est associée"""
        return bool(self.photo_personnalite)
    
 

    def get_absolute_photo_url(self):
        """
        Génère l'URL complète de la photo selon le format souhaité :
        /code_panneau/media/chemin_photo
        """
        if not self.photo_personnalite:
            return None
            
        # Si c'est déjà une URL complète
        if self.photo_personnalite.startswith(('http://', 'https://')):
            return self.photo_personnalite
            
        # Nettoyage du code QR pour l'URL
        qr_code = self.qr_code.replace('https://panneautage.bnetd.ci/', '').strip('/')
        
        # Construction de l'URL selon votre format demandé
        return f"/{qr_code}/media/{self.photo_personnalite.lstrip('/')}"
    
    @property
    def has_personnalite_photo(self):
        """Vérifie si une photo existe"""
        return bool(self.photo_personnalite)
 
   
class Suggestion(models.Model):
    voie = models.ForeignKey(
        Voie,
        on_delete=models.CASCADE,
        related_name='suggestions',
        db_column='voie_id'
    )
    nom_voie = models.CharField(max_length=255)
    qr_code_url = models.TextField()
    suggestion = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'suggestions'
        managed = False

    def save(self, *args, **kwargs):
        if not self.pk:  # Seulement lors du premier enregistrement
            if self.voie:
                self.nom_voie = self.voie.nom_voies
                self.qr_code_url = self.voie.qr_code
        super().save(*args, **kwargs)
