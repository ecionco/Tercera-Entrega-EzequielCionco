from django import forms
from .models import Trabajo, Solicitante

class TrabajoForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['titulo', 'descripcion', 'requisitos_excluyentes', 'requisitos_no_excluyentes', 'salario_ofrecido']

class SolicitanteForm(forms.ModelForm):
    class Meta:
        model = Solicitante
        fields = ['nombre', 'edad', 'habilidades']
