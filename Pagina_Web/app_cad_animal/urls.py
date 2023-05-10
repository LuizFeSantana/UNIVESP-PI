from django.urls import path

from.views import home,sobre,cadastrar,animais_cadastrados

urlpatterns = [
    path('',home),
    path('cadastrados',cadastrar),
    path('cadastrados',animais_cadastrados),
    path('sobre',sobre),
]