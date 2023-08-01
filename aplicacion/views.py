from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, redirect
from .forms import TrabajoForm, SolicitanteForm
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
from .forms import TrabajoForm, SolicitanteForm
from .models import Trabajo, Solicitante, Vinculacion
from django.utils import timezone

def insertar_datos(request):
    if request.method == 'POST':
        form_trabajo = TrabajoForm(request.POST)
        form_persona = SolicitanteForm(request.POST)
        if form_trabajo.is_valid() and form_persona.is_valid():
            trabajo = form_trabajo.save()
            persona = form_persona.save()
            return redirect('vincular_trabajo_persona', trabajo_id=trabajo.pk, persona_id=persona.pk)
    else:
        form_trabajo = TrabajoForm()
        form_persona = SolicitanteForm()
    
    return render(request, 'insertar_datos.html', {'form_trabajo': form_trabajo, 'form_persona': form_persona})

def vincular_trabajo_persona(request, trabajo_id, persona_id):
    trabajo = Trabajo.objects.get(pk=trabajo_id)
    persona = Solicitante.objects.get(pk=persona_id)

    if request.method == 'POST':
        salario_esperado = request.POST.get('salario_esperado', None)
        if salario_esperado:
            vinculacion = Vinculacion(
                trabajo=trabajo,
                persona_desocupada=persona,
                fecha_vinculacion=timezone.now(),
                estado='En proceso',
                salario_esperado=salario_esperado,
                comentarios=''
            )
            vinculacion.save()
    
    return render(request, 'vincular_trabajo_persona.html', {'trabajo': trabajo, 'persona': persona})
