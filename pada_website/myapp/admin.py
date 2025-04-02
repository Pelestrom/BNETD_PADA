from django.contrib import admin
from .models import Voie

@admin.register(Voie)
class VoieAdmin(admin.ModelAdmin):
    list_display = ('entites_territoriales_2', 'nom_voies', 'quartier', 'description')
    search_fields = ('nom_voies', 'quartier', 'entites_territoriales_2')
    list_filter = ('quartier', 'entites_territoriales_2')
    
    # Optionnel: configuration des champs pour la page d'édition
    fieldsets = (
        (None, {
            'fields': ('nom_voies', 'quartier', 'description')
        }),
        ('Coordonnées', {
            'fields': ('X', 'Y'),
            'classes': ('collapse',)
        }),
        ('Autres informations', {
            'fields': ('qr_code', 'entites_territoriales_2'),
            'classes': ('collapse',)
        }),
    )