from django import forms
from .models import Trabajo, Solicitante, Vinculacion

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['titulo', 'descripcion', 'requisitos_excluyentes', 'requisitos_no_excluyentes', 'salario_ofrecido']

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['nombre', 'edad', 'habilidades']
        
        
class VinculacionForm(forms.ModelForm):
    class Meta:
        model = Vinculacion
        fields = ['trabajo', 'job_solicitante', 'fecha_vinculacion', 'estado', 'salario_esperado','comentarios' ]
