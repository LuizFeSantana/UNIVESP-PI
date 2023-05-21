from django.views.generic.edit import CreateView

from .models import Animais, Usuario, Ongs, Servicos, Veterinario, Clinica, Localizacao, LarDefinitivo, LarTemporario

from django.urls import reverse_lazy

# Create your views here.

class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['Nome', 'cpf', 'rg', 'Funcao', 'email', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class OngsCreate(CreateView):
    model = Ongs
    fields = ['CNPJ', 'RazaoSocial', 'email', 'resp', 'telefone', 'endereco', 'cep']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class ClinicaCreate(CreateView):
    model = Clinica
    fields = ['CNPJ', 'RazaoSocial', 'medicoResp', 'endereco', 'bairro', 'estado', 'cep', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class VeterinarioCreate(CreateView):
    model = Veterinario
    fields = ['Nome', 'CRMV', 'celular', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')