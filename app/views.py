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

def lector(request):
    return render(request, 'lector.html')

def prestamos(request):
    lista = models.lector.objects.all()
    return render(request, 'Prestamos.html', {'lista': lista})

def guardaVisita(request):
    if 'nombre' in request.POST and 'fecha' in request.POST and 'telefono' in request.POST and 'direccion' in request.POST:
        nombre = request.POST['nombre']
        fecha = request.POST['fecha']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']

        p = models.visita(nombre = nombre,fecha = fecha, telefono = telefono, direccion = direccion)
        p.save()
        return render (request,'visita.html',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'visita.html', {'msg': 'No se puede realizar el registro'})

def consultaVisita(request):
    registro = models.visita.objects.all()
    return render(request,'consultaVisita.html',{"registro":registro})

def guardarlector(request):
    if 'Nombre' in request.POST and 'Edad' in request.POST and 'Domicilio' in request.POST and 'Cp' in request.POST and 'Telefono' in request.POST and 'Ocupacion' in request.POST and 'Esc_o_trab' in request.POST and 'Tel_esc' in request.POST and 'Dir_esc' in request.POST:
        Nombre = request.POST['Nombre']
        Edad = request.POST['Edad']
        Domicilio = request.POST['Domicilio']
        Cp = request.POST['Cp']
        Telefono = request.POST['Telefono']
        Ocupacion = request.POST['Ocupacion']
        Esc_o_trab = request.POST['Esc_o_trab']
        Tel_esc = request.POST['Tel_esc']
        Dir_esc = request.POST['Dir_esc']
        p = models.lector(Nombre = Nombre,Edad = Edad, Domicilio = Domicilio, Cp = Cp, Telefono = Telefono, Ocupacion= Ocupacion, Esc_o_trab = Esc_o_trab, Tel_esc = Tel_esc, Dir_esc = Dir_esc)
        p.save()
        return render (request,'lector.html',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'lector.html', {'msg': 'No se puede realizar el registro'})

def guardaLibro(request):
    if 'isbn' in request.POST and 'titulo' in request.POST and 'autor' in request.POST and 'editorial' in request.POST and 'edicion' in request.POST and 'fimp' in request.POST and 'tipo' in request.POST:
        isbn = request.POST['isbn']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        editorial = request.POST['editorial']
        edicion = request.POST['edicion']
        fimp = request.POST['fimp']
        tipo = request.POST['tipo']

        p = models.libros(isbn = isbn, titulo = titulo, autor = autor,editorial = editorial,edicion = edicion,fimp = fimp,tipo = tipo)
        p.save()
        return render (request,'ag_lib.html',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'ag_lib.html', {'msg': 'No se puede realizar el registro'})

def elimi(request):
    if 'idVisita' in request.POST:
        per = models.visita.objects.get(idVisita=request.POST['idVisita'])
        per.delete()
    return redirect('/menu/visita/consulta')


def guardarprestamos(request):
    if 'fecha' in request.POST and 'Fvencida' in request.POST:
        fecha=request.POST['Fecha']
        Fvencida=request.POST['Fvencida']
        p=models.prestamos(Fecha=Fecha,fechaVencida=Fvencida)
        p.save()
        return render (request, 'Prestamos.html',{'msg':'Registro realizado exitosamente'})
    else:
        return render(request,'Prestamos.html',{'msg':'Registro realizado exitosamente'})
