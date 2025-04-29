from django.contrib import admin
from .models import Voie
from .models import Suggestion

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
    
@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('nom_voie', 'date_creation', 'short_suggestion')
    list_filter = ('date_creation',)
    search_fields = ('nom_voie', 'suggestion')
    
    def short_suggestion(self, obj):
        return obj.suggestion[:50] + '...' if len(obj.suggestion) > 50 else obj.suggestion
    short_suggestion.short_description = 'Suggestion'