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
   
   
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))     

