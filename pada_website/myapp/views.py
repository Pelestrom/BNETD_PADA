from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Voie
from .forms import SuggestionForm

def home_view(request, qr_code):
    qr_code = qr_code.replace('https://panneautage.bnetd.ci/', '')
    full_qr_code = f"https://panneautage.bnetd.ci/{qr_code}"
    
    voie = get_object_or_404(Voie, qr_code=full_qr_code)
    return render(request, 'home.html', {
        'description_rue': voie.description,
        'nom_rue': voie.nom_voies,
        'quartier_rue': voie.quartier,
        'commune_rue': voie.entites_territoriales_2,
        'x': voie.X,
        'y': voie.Y,
        'qr_code': qr_code,
        # 'typologie': voie.typologie,
        # 'typologie_icon': typologie_icons.get(voie.typologie.lower(), 'ri-information-line')
    })
    
def redirect_view(request):
    # Logique de la vue de redirection
    return redirect('map')


@require_POST
def submit_suggestion(request, qr_code):
    # Nettoyez le qr_code comme dans home_view
    qr_code = qr_code.replace('https://panneautage.bnetd.ci/', '')
    full_qr_code = f"https://panneautage.bnetd.ci/{qr_code}"
    
    # Essaye de récupérer la voie associée au QR code
    try:
        voie = get_object_or_404(Voie, qr_code=full_qr_code)
    except Voie.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Voie not found'}, status=404)
    
    form = SuggestionForm(request.POST)
    
    if form.is_valid():
        # Crée une suggestion sans la sauvegarder tout de suite
        suggestion = form.save(commit=False)
        
        # Laisser le modèle gérer l'assignation de voie, nom_voie et qr_code_url
        suggestion.voie = voie
        
        # Sauvegarder la suggestion dans la base de données
        suggestion.save()
        
        # Retourner un message de succès
        return JsonResponse({'status': 'success'})
    
    # Si le formulaire est invalide, retourner les erreurs sous forme JSON
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)