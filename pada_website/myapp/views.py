from django.shortcuts import render, redirect, get_object_or_404
from .models import Rue

def map_view(request):
    return render(request, 'map.html')

def home_view(request):
    # Récupère l'ID depuis les paramètres de la requête GET
    rue_id = request.GET.get('id')
    
    # Si l'ID n'est pas présent dans la requête, renvoyer une erreur 404
    if not rue_id:
        return render(request, '404.html', status=404)

    # Récupère la rue correspondant à l'ID, ou renvoie une 404 si non trouvée
    rue = get_object_or_404(Rue, id=rue_id)

    # Récupération des informations de la rue
    description_rue = rue.description
    nom_rue = rue.nom_rue
    quartier_rue = rue.quartier
    commune_rue = rue.commune

    # Récupération des coordonnées et du niveau de zoom
    x = rue.x
    y = rue.y
    h = rue.h

    return render(request, 'home.html', {
        'description_rue': description_rue,
        'nom_rue': nom_rue,
        'quartier_rue': quartier_rue,
        'commune_rue': commune_rue,
        'x': x,
        'y': y,
        'h': h,
    })

def redirect_view(request):
    # Logique de la vue de redirection
    return redirect('map')
