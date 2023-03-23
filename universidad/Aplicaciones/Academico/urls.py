from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cursos/', views.cursos),
    path('registrar/', views.addCursoF),
    path('registrarCurso/', views.addCurso),
    path('editarCurso/<codigo>', views.editCurso),
    path('editaCurso/', views.editCursoPost),
    path('eliminarCurso/<codigo>', views.deleteCurso),
    path('buscar', views.buscarCurso),
    path('autenticar',views.autenticar),
    path('registrarUsuario',views.registrarF),
    path('registrarUsuarioForm',views.registrarUsuario),
    path('autenticar',views.autenticar),
    path('listadoUsuarios',views.listadoUsuarios),
    path('eliminarUsuario/<codigo>',views.eliminaUsuario),
    path('editarUsuario/<codigo>',views.registrarF),
    path('salir/',views.salir),
]
