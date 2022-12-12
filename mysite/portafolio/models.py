from django.db import models

# Create your models here.
# clase tabla
class Portadata(models.Model):
    foto= models.CharField(max_length=200)
    titulo= models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    tags= models.CharField(max_length=100)
    url=models.CharField(max_length=200)