# coding: utf-8
from django.db import models

class Lobby(models.Model):
    empresa = models.CharField('Nombre empresa', max_length=100)
    nombre = models.CharField('Nombre', max_length=100)
    apellido = models.CharField('Apellido', max_length=100, blank=True)
    email = models.EmailField('email', max_length=100)
    telefono = models.CharField('Telefono', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nombre

    def fecha_creado(self):
    	return self.created_at
    fecha_creado.short_description = "Fecha creado"