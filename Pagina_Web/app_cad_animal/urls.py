from django.urls import path

from .views import home,sobre, cad_animal, cadastro, tutor

urlpatterns = [
    path('', home),
    path('sobre', sobre),
    path('cad_animal', cad_animal),
    path('cadastro', cadastro),
    path('tutor', tutor),
]