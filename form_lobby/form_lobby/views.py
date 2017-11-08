# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LobbyForm


def lobby(request):
    if request.method == 'POST':
    	form = LobbyForm(request.POST)
    	if form.is_valid():
            empresa = form.cleaned_data['empresa']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono']

            asd = form.save()

            return HttpResponseRedirect('/gracias/')
        else:
            print "NO"
    else:
        form = LobbyForm()

    return render(request, 'lobby_form.html', {'form': form})

def gracias(request):
    return render(request, 'gracias.html')