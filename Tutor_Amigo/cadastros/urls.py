from django.urls import path

#importa as views criadas
from .views import UsuarioCreate, OngsCreate, ClinicaCreate, VeterinarioCreate

urlpatterns = [
    #path('endereço/', MinhasView.as_view(), name= 'nome da url')

    path('cadastros/tutor', UsuarioCreate.as_view(), name= 'cadastro-tutor'),
    path('cadastros/ong', OngsCreate.as_view(), name= 'cadastro-ong'),
    path('cadastros/clinica', ClinicaCreate.as_view(), name= 'cadastro-clinica'),
    path('cadastros/veterinario', VeterinarioCreate.as_view(), name= 'cadastro-veterinario'),
    
]