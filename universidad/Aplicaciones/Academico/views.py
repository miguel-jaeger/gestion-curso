from django.shortcuts import render
from .models import Curso


# Create your views here.
def home(request):
    listadoCursos= Curso.objects.all()
    return render(request, "gestionCurso.html", {"cursos":listadoCursos})