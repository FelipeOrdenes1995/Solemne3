from django.db import models
from django.db.models.deletion import CASCADE  


class Servicio(models.Model):
    #id --> numero autoincrementable, Django lo hace por nosotros
    nombre= models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Plan(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    servicio = models.ForeignKey(Servicio, on_delete=CASCADE)
    contenido = models.TextField(null=True, blank=True)
    
    
     
    def __str__(self):
        return self.nombre
