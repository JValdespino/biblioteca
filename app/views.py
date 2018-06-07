from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def visita(request):
    return render(request, 'visita.html')

def guardaVisita(request):
    if 'idVisita' in request.POST and 'nombre' in request.POST and 'fecha' in request.POST and 'telefono' in request.POST and 'direccion' in request.POST:
        idVisita = request.POST['idVisita']
        nombre = request.POST['nombre']
        fecha = request.POST['fecha']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']

        p = models.visita(idVisita = idVisita,nombre = nombre,fecha = fecha, telefono = telefono, direccion = direccion)
        p.save()
        return render (request,'visita.html',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'visita.html', {'msg': 'No se puede realizar el registro'})

def consultaVisita(request):
    registro = models.visita.objects.all()
    return render(request,'consultaVisita.html',{"registro":registro})