from datetime import date
from django.shortcuts import render
from . import models

# Create your views here.

def ejemplo(request):
    hoy = date.today()
    practicas= date(2024,4,1)
    dias=(practicas-hoy).days
    return render(request, "ejemplo.html", {"hoy": hoy, "dias":dias})

def usuario(request):
    datos= models.Test.objects.all()
    usuario=datos[0]
    
    contexto={}
    contexto["id"]=usuario.id
    contexto["nombre"]=usuario.nombre
    contexto["apellido1"]=usuario.apellido1
    contexto["apellido2"]=usuario.apellido2

    return render(request, "usuario.html", (contexto))
