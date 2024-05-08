from django import forms
from .models import infa, PublishedCode, Messenger

class InfaForm(forms.ModelForm):
    class Meta:
        model = infa
        fields = ['name', 'description']


class PublishedCodeForm(forms.ModelForm):
    class Meta:
        model = PublishedCode
        fields = ['code', 'description']


class MessengerForm(forms.ModelForm):
    class Meta:
        model = Messenger
        fields = ['content']