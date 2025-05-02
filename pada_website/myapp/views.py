from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse,Http404
from django.views.decorators.http import require_POST
from .models import Voie
from .forms import SuggestionForm
from django.http import FileResponse
import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings

def home_view(request, qr_code):
    # Nettoyage du QR code
    cleaned_qr = qr_code.replace('https://panneautage.bnetd.ci/', '').strip()
    full_qr_code = f"https://panneautage.bnetd.ci/{cleaned_qr}"
    
    # Récupération de la voie (maintenant utilisée dans le contexte)
    voie = get_object_or_404(Voie, qr_code=full_qr_code)
    
    # Construction du contexte en utilisant directement les attributs de 'voie'
    return render(request, 'home.html', {
        'description_rue': voie.description,
        'nom_rue': voie.nom_voies,
        'quartier_rue': voie.quartier,
        'commune_rue': voie.entites_territoriales_2,
        'x': voie.X,
        'y': voie.Y,
        'qr_code': cleaned_qr,
        'photo_personnalite': voie.get_absolute_photo_url(),
        'has_personnalite_photo': voie.has_personnalite_photo,
        'voie': voie,  # Ajout de l'objet complet au contexte si nécessaire
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


def serve_personnalite_photo(request, qr_code, photo_path):
    # Validez que le QR code correspond à un panneau existant
    voie = get_object_or_404(Voie, qr_code=f"https://panneautage.bnetd.ci/{qr_code}")
    
    # Chemin complet du fichier
    file_path = os.path.join(settings.MEDIA_ROOT, photo_path)
    
    # Vérifiez que le fichier existe et est dans le bon dossier
    if not os.path.exists(file_path) or not file_path.startswith(settings.MEDIA_ROOT):
        raise Http404("Photo non trouvée")
    
    return FileResponse(open(file_path, 'rb'))