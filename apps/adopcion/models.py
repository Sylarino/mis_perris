from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    run = models.CharField(max_length=10)
    fNacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    region = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    tipoVivienda = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre