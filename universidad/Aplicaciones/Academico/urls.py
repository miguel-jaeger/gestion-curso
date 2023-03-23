from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('cursos/', views.cursos,name="cursos"),
    path('registrar/', views.addCursoF,name="registrar"),
    path('registrarCurso/', views.addCurso,name="registrarCurso"),
    path('editarCurso/<codigo>', views.editCurso,name="editarCurso"),
    path('editaCurso/', views.editCursoPost,name="editarCursoPost"),
    path('eliminarCurso/<codigo>', views.deleteCurso,name="eliminarCurso"),
    path('buscar', views.buscarCurso,name="buscar"),
    path('autenticar',views.autenticar,name="autenticar"),
    path('registrarUsuario',views.registrarF,name="registrarUsuarioView"),
    path('registrarUsuarioForm',views.registrarUsuario,name="registrarUsuarioForm"),
    path('autenticar/',views.autenticar,name="autenticar"),
    path('listadoUsuarios',views.listadoUsuarios,name="listadoUsuarios"),
    path('eliminarUsuario/<codigo>',views.eliminaUsuario,name="eliminarUsuario"),
    path('editarUsuario/<codigo>',views.registrarF,name="editarUsuario"),
    path('salir/',views.salir,name="salir"),
]
