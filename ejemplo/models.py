from django.db import models

# Create your models here.

class Test(models.Model): 
    id = models.IntegerField(primary_key=True) 
    nombre = models.CharField(max_length=50) 
    apellido1 = models.CharField(max_length=50) 
    apellido2 = models.CharField(max_length=50)