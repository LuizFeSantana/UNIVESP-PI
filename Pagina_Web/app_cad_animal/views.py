from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def cadastrar(request):
    return render(request,'cadastro.html')

def animais_cadastrados(request):
    return render(request,'cad_animal.html')

def sobre(request):
    return render(request,'sobre.html')