from django.contrib import admin
from Aplicaciones.Academico import models
from .models import Curso
# Register your models here.
#admin.site.register(Curso)

@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre', 'creditos']
    search_fields = ['codigo', 'nombre']
    # inlines = [NoteInline]
    # autocomplete_fields = ['nombre']
