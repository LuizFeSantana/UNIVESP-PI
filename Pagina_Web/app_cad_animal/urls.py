from django.urls import path

from .views import home,sobre

urlpatterns = [
    path('', home),
    path('sobre', sobre),
]