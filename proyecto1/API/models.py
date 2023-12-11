from django.db import models

class Ejemplo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def str(self):
        return self.nombre

# Create your models here.
