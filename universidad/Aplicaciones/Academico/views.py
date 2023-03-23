from django.shortcuts import render, redirect
from .models import Curso
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):   
    return render(request, "inicio.html")

def cursos(request):
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

def registrarF(request):
    
    if request.method=='GET':
        return render(request, "registro.html")
    else:
            if request.POST['password1']==request.POST['password2']:
                try:
                    #registrar usuario
                    user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                    user.save()
                    login(request,user)
                    return redirect("/listadoUsuarios",{"msg":"Usuario registrado satisfactoriamente"})
                except:
                    return render(request, "registro.html", {"error": "El usuario ya existe"})
            
            else:
                return render(request, "registro.html", {"error": "Las contraseñas no coinciden"})

def registrarUsuario(request):
    
    if request.method=='GET':
        return render(request, "registroUsuario.html")
    else:
            if request.POST['password1']==request.POST['password2']:
                try:
                    #registrar usuario
                    user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                    user.save()
                    login(request,user)
                    return redirect("/listadoUsuarios",{"msg":"Usuario registrado satisfactoriamente"})
                except:
                    return render(request, "registroUsuario.html", {"error": "El usuario ya existe"})
            
            else:
                return render(request, "registroUsuario.html", {"error": "Las contraseñas no coinciden"})

def listadoUsuarios(request):

    listadoUsuarios = User.objects.all()
    return render(request, "listadoUsuarios.html", {"usuarios": listadoUsuarios})


def eliminaUsuario(request, codigo):
    usuario = User.objects.get(id=codigo)
    usuario.delete()
    return redirect("/listadoUsuarios")

def salir(request):
    logout(request)
    return redirect("/")

def autenticar(request):
    
    if request.method=='GET':
        return render(request, "registro.html")
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password1'])
        if user is None:
            return render(request, "registro.html",{"error":"Usuario o password incorrectoa"})
        else:
            login(request,user)
            return redirect("/")
        
