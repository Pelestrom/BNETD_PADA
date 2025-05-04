from django import forms
from .models import Suggestion
from django.contrib.auth.forms import AuthenticationForm

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['suggestion']
        widgets = {
            'suggestion': forms.Textarea(attrs={
                'class': 'suggestion-input',
                'placeholder': 'Votre suggestion pour cette voie...',
                'rows': 4
            })
        }
   
   
 