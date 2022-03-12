from django.db import models
# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique = True)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.alias}"

class Poke(models.Model):
    autor = models.ForeignKey(Usuario,related_name='pokes_hechos', on_delete=models.CASCADE)
    recipiente = models.ForeignKey(Usuario, related_name = 'pokes_recibidos', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
