from django.db import models

# Create your models here.
# create comment to prove merge command
class Curso(models.Model):
    #codigo = models.CharField(max_length=60, unique=True)
    #codigo = models.CharField(primary_key=True, max_length=6)
    codigo = models.CharField(max_length=60, unique=True)
    nombre= models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0}" "({1})"
        return texto.format(self.nombre,self.creditos)
