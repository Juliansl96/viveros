from django.db import models

class Labor(models.Model):
    codigo = models.CharField(max_length=6,unique=True)
    fecha = models.DateField()
    descripcion = models.TextField(max_length=500)

    def __str__(self):
        
        return f'Codigo:{self.codigo} Fecha: {self.fecha}, Descripcion: {self.descripcion}'