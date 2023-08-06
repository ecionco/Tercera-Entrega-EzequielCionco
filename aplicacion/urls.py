from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name = "inicio"),
    path('solicitante/', solicitante, name = "solicitante"),
    path('trabajos/', trabajos, name = "trabajo"),
    path('vinculacion/', vinculacion, name = "vinculacion"),
    
    path('vinculacion_form/', vinculacionForm, name = "vinculacion_form"),
    path('trabajo_form/', trabajoForm, name = "trabajo_form"),
    path('solicitante_form/', solicitanteForm, name = "solicitante_form"),
    
    path('buscar_habilidades/', buscarHabilidades, name = "buscar_habilidades"),
    path('buscar_habilidades2/', buscarHabilidades2, name = "buscar_habilidades2"),
    path('buscar_titulo/', buscarTitulo, name = "buscar_titulo"),
    path('buscar_titulo2/', buscarTitulo2, name = "buscar_titulo2"),
]