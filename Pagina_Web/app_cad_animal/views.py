from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def sobre(request):
    return render(request,'sobre.html')

def cad_animal(request):
    return render(request,'cad_animal.html')

def tutor(request):
    return render(request,'tutor.html')

def cadastro(request):
    return render(request,'cadastro.html')