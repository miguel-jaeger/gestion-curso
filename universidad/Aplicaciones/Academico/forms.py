from django.forms import ModelForm

from .models import Curso

class cursoForm(ModelForm):
    class Meta:
        model= Curso
        fields = ['codigo','nombre', 'creditos']



