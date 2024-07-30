from django.db import models

# Create your models here.

#creacion de clase persona con sus atributos con herencia de clase models
class Persona (models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    



