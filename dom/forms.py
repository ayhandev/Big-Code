from django import forms
from .models import infa

class InfaForm(forms.ModelForm):
    class Meta:
        model = infa
        fields = ['name', 'description']
