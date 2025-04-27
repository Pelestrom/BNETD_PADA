from django.shortcuts import render, get_object_or_404, redirect
from .models import Voie

def home_view(request, qr_code):
    full_qr_code = f"https://panneautage.bnetd.ci/{qr_code}"
    voie = get_object_or_404(Voie, qr_code=full_qr_code)

    # Définition des icônes en fonction de la typologie
    typologie_icons = {
        'personnalité communale': 'ri-community-line',
        'personnalité nationale': 'ri-flag-line',
        'personnalité internationale': 'ri-global-line',
        'élément de la nature': 'ri-leaf-line',
        'riverain': 'ri-home-4-line',
        'concept': 'ri-lightbulb-line',
        'valeur morale': 'ri-heart-line',
        'continent': 'ri-earth-line',
        'pays': 'ri-map-pin-line',
        'ville': 'ri-building-line'
    }

    return render(request, 'home.html', {
        'description_rue': voie.description,
        'nom_rue': voie.nom_voies,
        'quartier_rue': voie.quartier,
        'commune_rue': voie.entites_territoriales_2,
        'x': voie.X,
        'y': voie.Y,
        'qr_code': voie.qr_code,
        'typologie': voie.typologie,
        'typologie_icon': typologie_icons.get(voie.typologie.lower(), 'ri-information-line')
    })
def redirect_view(request):
    # Logique de la vue de redirection
    return redirect('map')


