from django.shortcuts import render, redirect
from .models import Curso
from django.db import IntegrityError


# Create your views here.
def home(request):
    listadoCursos = Curso.objects.all()
    return render(request, "gestionCurso.html", {"cursos": listadoCursos})


def addCursoF(request):
    return render(request, "adicionarCurso.html")


def addCurso(request):
    try:
        # código de inserción aquí
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        credito = request.POST['creditos']

        Curso.objects.create(codigo=codigo, nombre=nombre, creditos=credito)
        return redirect("/")
    except IntegrityError as e:
        if 'UNIQUE constraint failed' in str(e):
        # manejo de excepción de campo único duplicado aquí
            return render(request, "adicionarCurso.html",{"error":"Ya existe ese código"})
        else: "Field 'creditos' expected a number but got" in str(e)
        return render(request, "adicionarCurso.html",{"error":"El campo creditos debe ser entero"})
    #except Exception as e:
     #   return render(request, "adicionarCurso.html",{"error":"otro error"})


def editCurso(request, codigo):
    curso = Curso.objects.get(id=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editCursoPost(request):
    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    credito = request.POST['creditos']
    id = request.POST['id']

    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = credito
    curso.save()
    return redirect("/")


def deleteCurso(request, codigo):
    curso = Curso.objects.get(id=codigo)
    curso.delete()
    return redirect("/")


def buscarCurso(request):
    buscar = request.POST['buscar']
    filter = Curso.objects.filter(nombre__contains=buscar)
    return render(request, "gestionCurso.html", {"cursos": filter, "criterio": buscar})
