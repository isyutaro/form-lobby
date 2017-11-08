from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class LobbyForm(forms.Form):
    empresa = forms.CharField(label='Nombre empresa: ', max_length=100)
    nombre = forms.CharField(label='Nombre: ', max_length=100)
    apellido = forms.CharField(label='Apellido', max_length=100, required=False)
    email = forms.EmailField(label='email: ', max_length=100, required=False)
    telefono = forms.IntegerField(label='Telefono: ', required=False)