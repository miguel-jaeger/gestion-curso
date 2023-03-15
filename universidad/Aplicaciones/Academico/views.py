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

        if(not credito.isnumeric()):
            return render(request, "adicionarCurso.html",{"error":"El campo creditos debe ser entero positivo"})
            
        credito=int(credito)
        

        Curso.objects.create(codigo=codigo, nombre=nombre, creditos=credito)
        return redirect("/")
    except IntegrityError as e:
        if 'UNIQUE constraint failed' in str(e):
        # manejo de excepción de campo único duplicado aquí
            return render(request, "adicionarCurso.html",{"error":"Ya existe ese código"})
        
    #except Exception as e:
     #   return render(request, "adicionarCurso.html",{"error":"otro error"})


def editCurso(request, codigo):
    curso = Curso.objects.get(id=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})


def editCursoPost(request):

    try:
        id = request.POST['id']
        curso = Curso.objects.get(id=id)
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        credito = request.POST['creditos']
        

        if(not credito.isnumeric()):
                return render(request, "edicionCurso.html",{"curso": curso,"error":"El campo creditos debe ser entero positivo"})

        credito=int(credito)
       
        curso.nombre = nombre
        curso.creditos = credito
        curso.save()
        return redirect("/")

    except IntegrityError as e:
        id = request.POST['id']
        curso = Curso.objects.get(id=id)
        if 'UNIQUE constraint failed' in str(e):
        # manejo de excepción de campo único duplicado aquí
            return render(request, "edicionCurso.html",{"curso": curso,"error":"Ya existe ese código"})


def deleteCurso(request, codigo):
    curso = Curso.objects.get(id=codigo)
    curso.delete()
    return redirect("/")


def buscarCurso(request):
    buscar = request.POST['buscar']
    filter = Curso.objects.filter(nombre__contains=buscar)
    return render(request, "gestionCurso.html", {"cursos": filter, "criterio": buscar})
