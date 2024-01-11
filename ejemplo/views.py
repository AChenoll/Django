from datetime import date
from django.shortcuts import render

# Create your views here.

def ejemplo(request):
    hoy = date.today()
    practicas= date(2024,4,1)
    dias=(practicas-hoy).days
    return render(request, "ejemplo.html", {"hoy": hoy, "dias":dias})