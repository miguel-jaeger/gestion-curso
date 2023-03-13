from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrar/', views.addCursoF),
    path('registrarCurso/', views.addCurso),
    path('editarCurso/<codigo>', views.editCurso),
    path('editaCurso/', views.editCursoPost),
    path('eliminarCurso/<codigo>', views.deleteCurso),
    path('buscar', views.buscarCurso),
]
