# coding: utf-8
from django import forms
from .models import Lobby


class LobbyForm(forms.ModelForm):
    class Meta:
        model = Lobby
        exclude = ('created_at', )

    empresa = forms.CharField(label='Nombre empresa', max_length=100)
    nombre = forms.CharField(label='Nombre', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100, required=False)
    email = forms.EmailField(label='email', max_length=100)
    telefono = forms.IntegerField(label='Telefono')
