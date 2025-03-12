from django.contrib import admin
from .models import Rue

@admin.register(Rue)
class RueAdmin(admin.ModelAdmin):
    list_display = ('commune', 'nom_rue', 'quartier')
    search_fields = ('nom_rue', 'quartier')

# Alternative way to register the model:
# admin.site.register(Rue, RueAdmin)
