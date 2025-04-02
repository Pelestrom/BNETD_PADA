from django.shortcuts import render, redirect, get_object_or_404
from .models import Voie

def home_view(request, qr_code):
    voie = get_object_or_404(Voie, qr_code=qr_code)
    # Récupération des informations de la voie
    return render(request, 'home.html', {
        'description_rue': voie.description,
        'nom_rue': voie.nom_voies,
        'quartier_rue': voie.quartier,
        'commune_rue': voie.entites_territoriales_2,
        'x': voie.X,
        'y': voie.Y,
        'qr_code': voie.qr_code,
    })

def redirect_view(request):
    # Logique de la vue de redirection
    return redirect('map')