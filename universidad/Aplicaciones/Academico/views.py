from django.shortcuts import render,redirect
from .models import Curso


# Create your views here.
def home(request):
    listadoCursos= Curso.objects.all()
    return render(request, "gestionCurso.html", {"cursos":listadoCursos})

def addCursoF(request):
    return render(request, "adicionarCurso.html")


def addCurso(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    credito=request.POST['creditos']

    Curso.objects.create(codigo=codigo,nombre=nombre,creditos=credito)
    return redirect("/")


def editCurso(request,codigo):
    curso= Curso.objects.get(codigo=codigo)    
    return render(request,"edicionCurso.html",{"curso":curso}) 


def editCursoPost(request):
    codigo=request.POST['codigo']
    nombre=request.POST['nombre']
    credito=request.POST['creditos']

    curso= Curso.objects.get(codigo=codigo)
    curso.nombre=nombre
    curso.creditos=credito
    curso.save()
    return redirect("/")



def deleteCurso(request,codigo):
    curso= Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect("/")

def buscarCurso(request):
    buscar = request.POST['buscar']
    filter = Curso.objects.filter(nombre__contains = buscar)
    return render(request, "gestionCurso.html", {"cursos":filter})

