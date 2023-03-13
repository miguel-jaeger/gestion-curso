from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.addCurso),
    path('editarCurso/<codigo>', views.editCurso),
    path('editaCurso/', views.editCursoPost),
    path('eliminarCurso/<codigo>', views.deleteCurso),
]
