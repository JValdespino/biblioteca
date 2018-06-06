from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
from . import persona
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def nombre(request):
    valores = range(10)
    p = persona.persona()
    p.iniciar(1,'Jesus')

    p2 = persona.persona()
    p2.iniciar(2,'Juan')

    personas = [p,p2]
    return render(request, 'nombre.html', {'valores':personas})

def esclava(request):
    return render(request, 'esclavo.html')

def sumar (request):
    if 'num1' in request.POST and 'num2' in request.POST:
        n1 = request.POST['num1']
        n2 = request.POST['num2']
        
        if len(n1)<=0 and len(n2)<=0:
            return render(request,'esclavo.html')
        suma = int(n1) + int(n2)
        return render (request,'esclavo.html',{'suma':suma, 'num1':n1,'num2':n2})
    else:
        return render(request, 'esclavo.html')

def guardarPersona (request):
    if 'idPersona' in request.POST and 'nombre' in request.POST and 'edad' in request.POST:
        idPersona = request.POST['idPersona']
        nombre = request.POST['nombre']
        edad = request.POST['edad']

        p= models.persona(idPersona = idPersona,nombre = nombre,edad = edad)
        p.save()
        return render (request,'regPersona.html',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'regPersona.html', {'msg': 'No se puede realizar el registro'})

def consulta(request):
    registro = models.persona.objects.all()
    return render(request,'consulta.html',{"registro":registro})

def modificacion(request):
    if 'idPersona' in request.POST:
        registro = models.persona.objects.get(idPersona=request.POST['idPersona'])
        return render(request,'modificacion.html',{"reg":registro})
    else:
        return redirect('consulta/')

def modificar(request):
    if 'idPersona' in request.POST and 'nombre' in request.POST and 'edad' in request.POST:
        p = models.persona(idPersona = request.POST['idPersona'])
        p.nombre=request.POST['nombre']
        p.edad=request.POST['edad']
        p.save()
    return redirect('/hola/consulta', {'op':'Actualizacion Realizada'})
