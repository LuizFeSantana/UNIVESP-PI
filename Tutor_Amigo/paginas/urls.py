from django.urls import path

#importa as views criadas
from .views import PaginaInicial

urlpatterns = [
    #path('endereço/', MinhasView.as_view(), name= 'nome da url')

    path('', PaginaInicial.as_view(), name= 'inicio'),
]