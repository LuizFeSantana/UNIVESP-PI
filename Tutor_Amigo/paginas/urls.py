from django.urls import path

#importa as views criadas
from .views import PaginaInicial
from .views import Sobre
from .views import Cad_Animal
from .views import Parceiros
from .views import Login
from .views import Cadastro

urlpatterns = [
    #path('endereço/', MinhasView.as_view(), name= 'nome da url')

    path('', PaginaInicial.as_view(), name= 'inicio'),
    path('sobre/', Sobre.as_view(), name= 'sobre'),
    path('cad_animal/', Cad_Animal.as_view(), name= 'cad_animal'),
    path('parceiros/', Parceiros.as_view(), name= 'parceiros'),
    path('login/', Login.as_view(), name= 'login'),
    path('cadastro/', Cadastro.as_view(), name= 'cadastro'),
]