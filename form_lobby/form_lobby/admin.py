# coding: utf-8
from django.contrib import admin
from models import Lobby


@admin.register(Lobby)
class LobbyAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'empresa', 'email', 'telefono', 'fecha_creado')
	date_hierarchy = 'created_at'