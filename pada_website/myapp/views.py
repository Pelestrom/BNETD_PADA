from django.shortcuts import render, get_object_or_404, redirect
from .models import Voie

def home_view(request, qr_code):
    # Construire le qr_code complet à partir de l'ID fourni
    full_qr_code = f"https://panneautage.bnetd.ci/{qr_code}"
    voie = get_object_or_404(Voie, qr_code=full_qr_code)

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


