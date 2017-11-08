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
        form = LobbyForm()

    return render(request, 'lobby_form.html', {'form': form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/gracias/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'lobby_form.html', {'form': form})

def gracias(request):
    return render(request, 'gracias.html')
