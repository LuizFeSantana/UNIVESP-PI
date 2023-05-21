from django.urls import path

#importa as views criadas
from .views import UsuarioCreate, OngsCreate, ClinicaCreate, VeterinarioCreate
from .views import UsuarioUpdate, OngsUpdate, ClinicaUpdate, VeterinarioUpdate

urlpatterns = [
    #path('endereço/', MinhasView.as_view(), name= 'nome da url')

    path('cadastros/tutor', UsuarioCreate.as_view(), name= 'cadastro-tutor'),
    path('cadastros/ong', OngsCreate.as_view(), name= 'cadastro-ong'),
    path('cadastros/clinica', ClinicaCreate.as_view(), name= 'cadastro-clinica'),
    path('cadastros/veterinario', VeterinarioCreate.as_view(), name= 'cadastro-veterinario'),
    
    path('editar/tutor/<int:pk>/', UsuarioUpdate.as_view(), name= 'editar-tutor'),
    path('editar/ong/<int:pk>/', OngsUpdate.as_view(), name= 'editar-ong'),
    path('editar/clinica/<int:pk>/', ClinicaUpdate.as_view(), name= 'editar-clinica'),
    path('editar/veterinario/<int:pk>/', VeterinarioUpdate.as_view(), name= 'editar-veterinario'),
]