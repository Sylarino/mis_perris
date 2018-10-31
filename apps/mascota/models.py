from django.db import models

from apps.adopcion.models import Persona

# Create your models here.

class Mascota(models.Model):
    
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    descripcion = models.TextField()
    estado = models.CharField(max_length=10)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}' .format(self.nombre, self.persona)
        #cadena = self.nombre+" adoptante: "+self.persona
        #return cadena