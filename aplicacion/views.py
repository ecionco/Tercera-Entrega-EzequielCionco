from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from .forms import TrabajoForm, SolicitanteForm, VinculacionForm
from .models import Trabajo, Solicitante, Vinculacion
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html" )

def trabajos(request):
    ctx = {"trabajo": Trabajo.objects.all()}
    return render(request, "aplicacion/trabajos.html", ctx )

def solicitante(request):
    ctx = {"solicitante": Solicitante.objects.all()}
    return render(request, "aplicacion/solicitante.html", ctx )

def vinculacion(request):
    ctx = {"vinculacion": Vinculacion.objects.all()}
    return render(request, "aplicacion/vinculacion.html", ctx )

from django.shortcuts import render, redirect
from .forms import TrabajoForm, SolicitanteForm, VinculacionForm
from .models import Trabajo, Solicitante, Vinculacion
from django.utils import timezone

def solicitanteForm(request):
    if request.method == "POST":
        miForm = SolicitanteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            solicitante = Solicitante(nombre=informacion['nombre'], edad=informacion['edad'], habilidades=informacion['habilidades'])
            solicitante.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = SolicitanteForm()
        
    return render(request, "aplicacion/solicitanteForm.html", {"form":miForm})
    

def trabajoForm(request):
    if request.method == "POST":
        miForm = TrabajoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            trabajo = Trabajo(titulo=informacion['titulo'], descripcion=informacion['descripcion'], requisitos_excluyentes=informacion['requisitos_excluyentes'], requisitos_no_excluyentes=informacion['requisitos_no_excluyentes'], salario_ofrecido=informacion['salario_ofrecido'])
            trabajo.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = TrabajoForm()
    return render(request, "aplicacion/trabajoForm.html", {"form":miForm} )   
   

def vinculacionForm(request):
    if request.method == "POST":
        miForm = VinculacionForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            vinculacion = Vinculacion(trabajo=informacion['trabajo'], job_solicitante=informacion['job_solicitante'], fecha_vinculacion=informacion['fecha_vinculacion'], estado=informacion['estado'], salario_esperado=informacion['salario_esperado'], comentarios=informacion['comentarios'])
            vinculacion.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = VinculacionForm()
        
    return render(request, "aplicacion/vinculacionForm.html", {"form":miForm})   


def buscarHabilidades(request):
    return render(request, "aplicacion/buscarHabilidades.html")

def buscarHabilidades2(request):
    if request.GET['habilidades']:
        habilidades = request.GET['habilidades']
        solicitante = Solicitante.objects.filter(habilidades__icontains=habilidades)
        return render(request, "aplicacion/resultadosHabilidades.html", {"habilidades": habilidades, "solicitante":solicitante})
    
    
def buscarTitulo(request):
    return render(request, "aplicacion/buscarTitulo.html")

def buscarTitulo2(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        trabajo = Trabajo.objects.filter(titulo__icontains=titulo)
        return render(request, "aplicacion/resultadosTitulo.html", {"titulo": titulo, "trabajo":trabajo} )
    
   
