from django.shortcuts import render
from .models import Curso


# Create your views here.
def home(request):
    cursos= Curso.objects.all()
    return render(request, "gestionCurso.html", {"listado":cursos})