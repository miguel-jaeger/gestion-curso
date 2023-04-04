from django.shortcuts import get_object_or_404, render, redirect
from .models import Curso
from django.db import IntegrityError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import cursoForm


# Create your views here.
def home(request):   
    return render(request, "inicio.html")

""" CURSOS FUNCTIONS"""
@login_required
def cursos(request):
    listadoCursos = Curso.objects.all()
    return render(request, "gestionCurso.html", {"cursos": listadoCursos})

@login_required
def addCursoF(request):
    if request.method=="GET":        
        return render(request, "adicionarCurso.html")
    else:
        try:                        
            if 'id' in request.POST and request.POST['id'] != "":                
                curso = get_object_or_404(Curso,pk=int(request.POST['id']))
                form = cursoForm(request.POST, instance=curso)
                form.save()
                return redirect('/cursos')          
            else:
                form = cursoForm(request.POST)
                form.save()
                return redirect('/cursos')
        except ValueError:
            print(ValueError)
            return render(request, "adicionarCurso.html",{"error":"Proveer datos válidos"})
        
@login_required
def cursoDetalle(request,id):
    curso = get_object_or_404(Curso,pk=id)
    return render(request, "cursoDetalles.html", {"curso": curso})

@login_required
def deleteCurso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect("/cursos")

@login_required
def buscarCurso(request):
    buscar = request.POST['buscar']
    filter = Curso.objects.filter(nombre__contains=buscar)
    return render(request, "gestionCurso.html", {"cursos": filter, "criterio": buscar})

"""USUARIOS FUNCTIONS"""
def registrarF(request):
    
    if request.method=='GET':
        return render(request, "registroUsuario.html")
    else:

            #user = get_object_or_404(User,pk=id)
            
            if request.POST['password1']==request.POST['password2']:
                try:
                    #registrar usuario
                    user=User.objects.create(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
                    user.save()
                    login(request,user)
                    return redirect("/usuario/listado",{"msg":"Usuario registrado satisfactoriamente"})
                except:
                    return render(request, "registro.html", {"error": "El usuario ya existe"})
            
            else:
                return render(request, "registro.html", {"error": "Las contraseñas no coinciden"})


def registrarUsuario(request):
    
    if request.method=='GET':
        return render(request, "/usuario/listado.html")
    else:
            if request.POST['password1']==request.POST['password2']:
                try:
                    #registrar usuario
                    user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                    user.save()
                    login(request,user)
                    return redirect("/usuario/listado",{"msg":"Usuario registrado satisfactoriamente"})
                except:
                    return render(request, "registroUsuario.html", {"error": "El usuario ya existe"})
            
            else:
                return render(request, "registroUsuario.html", {"error": "Las contraseñas no coinciden"})

def editaUsuario(request):
    User.objects.filter(id=request.POST['id']).update(username=request.POST['username'],first_name=request.POST['first_name'],last_name=request.POST['last_name'])
    #user.save()
    return redirect("/usuario/listado",{"msg":"Usuario actualizado satisfactoriamente"})

@login_required
def listadoUsuarios(request):
    listadoUsuarios = User.objects.all()
    return render(request, "listadoUsuarios.html", {"usuarios": listadoUsuarios})

@login_required
def buscarUsuario(request,id):
    usuario = User.objects.get(id=id)
    return render(request, "editarUsuario.html", {"user": usuario})


def eliminaUsuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect("/usuario/listado")

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
        

def error_404_view(request, exception):    
    
    return render(request,'404.html')