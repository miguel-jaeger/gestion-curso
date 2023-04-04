from django.urls import path
from . import views
from django.conf.urls import handler404


urlpatterns = [
    path('', views.home,name="home"),
    # CURSOS 
    path('cursos/', views.cursos,name="cursos"),
    path('cursos/adicionar', views.addCursoF,name="registrar"),
    path('cursos/<int:id>/',  views.cursoDetalle, name="cursosdetalle"),
    path('cursos/<int:id>/editar',  views.editCursoF, name="cursoeditar"),
    path('cursos/<int:id>/eliminar',  views.deleteCurso, name="cursoeliminar"),
    #path('registrarCurso/', views.addCurso,name="registrarCurso"),
    #path('editarCurso/<codigo>', views.editCurso,name="editarCurso"),
    #path('editaCurso/', views.editCursoPost,name="editarCursoPost"),
    #path('eliminarCurso/<codigo>', views.deleteCurso,name="eliminarCurso"),
    #path('buscar', views.buscarCurso,name="buscar"),
    # USUARIOS
    path('autenticar',views.autenticar,name="autenticar"),
    path('usuario',views.registrarF,name="registrarUsuario"),
    path('registrarUsuarioForm',views.registrarUsuario,name="registrarUsuarioForm"),
    path('autenticar/',views.autenticar,name="autenticar"),
    path('usuario/listado',views.listadoUsuarios, name="listadoUsuarios"),
    path('usuario/<int:id>/eliminar',views.eliminaUsuario,name="eliminarUsuario"),
    path('usuario/<int:id>/editar', views.buscarUsuario,name="editarUsuario"),
    path('usuario/editar', views.editaUsuario,name="editarUsuario"),
    path('salir/',views.salir,name="salir"),

]

handler404 = 'Aplicaciones.Academico.views.error_404_view'

