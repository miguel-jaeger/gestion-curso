from django.shortcuts import render,redirect
from .models import Curso


# Create your views here.
def home(request):
    listadoCursos= Curso.objects.all()
    return render(request, "gestionCurso.html", {"cursos":listadoCursos})

def addCurso(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    credito=request.POST['creditos']

    Curso.objects.create(codigo=codigo,nombre=nombre,creditos=credito)
    return redirect("/")
