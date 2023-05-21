from django.views.generic.edit import CreateView

from .models import Animais, Usuario, Ongs, Servicos, Veterinario, Clinica, Localizacao, LarDefinitivo, LarTemporario

from django.urls import reverse_lazy

# Create your views here.

class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['Nome', 'cpf', 'rg', 'Funcao']