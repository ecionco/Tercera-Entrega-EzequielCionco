from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name = "inicio"),
    path('solicitante/', solicitante, name = "solicitante"),
    path('trabajos/', trabajos, name = "trabajo"),
    path('vinculacion/', vinculacion, name = "vinculacion"),
]