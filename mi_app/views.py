from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"Hola mundo {fecha_hora_ahora}")

def saludar_a(resquet, nombre):
    return HttpResponse(f"Hola como estas {nombre.capitalize()}")

