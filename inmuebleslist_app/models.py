from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User
from user_app.models import Account
# Create your models here.

class Empresa(models.Model):
    nombre=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
class Inmueble(models.Model):
    direccion = models.CharField(max_length=255)
    pais=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    imagen=models.CharField(max_length=900)
    avg_calificacion=models.FloatField(default=0)
    number_calification=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    empresa_id=models.ForeignKey(Empresa,on_delete=models.CASCADE,related_name="empresas")
    
    def __str__(self):
        return self.direccion
    
    
class Comentario(models.Model):
    calificacion=models.PositiveIntegerField()
    texto=models.CharField(max_length=200 , null=True, blank=True)
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    inmueble_id=models.ForeignKey(Inmueble, on_delete=models.CASCADE,related_name="comentarios")
    comentario_user=models.ForeignKey(Account, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return str(self.calificacion)
    

    