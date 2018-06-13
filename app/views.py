from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
# from django.template.loader import get_template
# from django.template import Context
from . import models

# Create your views here.

def index(request):
    return render(request, 'index.html')

def libro(request):
    return render(request, 'ag_lib.html')

def libroEdita(request):
    if 'isbn' in request.POST:
        registro = models.libros.objects.get(isbn=request.POST['isbn'])
        return render(request, 'modificacionLibro.html',{"reg":registro})

def modificaLibro(request):
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
        return redirect ('/menu/libro/consulta',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'ag_lib.html', {'msg': 'No se puede realizar el registro'})

def eliminaLibro(request):
    if 'isbn' in request.POST:
        eli = models.libros.objects.get(isbn=request.POST['isbn'])
        eli.delete()
    return redirect('/menu/libro/consulta')

def visita(request):
    return render(request, 'visita.html')

def lector(request):
    return render(request, 'lector.html')

def prestamos(request):
    lista = models.lector.objects.all()
    lista1 = models.libros.objects.all()
    return render(request, 'Prestamos.html', {'lista': lista,'lista1':lista1})

def editaVisita(request):
    if 'idVisita' in request.POST:
        registro = models.visita.objects.get(idVisita=request.POST['idVisita'])
        return render(request, 'modificacionVisita.html',{"reg":registro})

def modificaVisita(request):
    if  'idVisita' in request.POST and 'nombre' in request.POST and 'fecha' in request.POST and 'telefono' in request.POST and 'direccion' in request.POST:
        idVisita = request.POST['idVisita']
        nombre = request.POST['nombre']
        fecha = request.POST['fecha']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        p = models.visita(idVisita = idVisita,nombre = nombre,fecha = fecha, telefono = telefono, direccion = direccion)
        p.save()
        return redirect ('/menu/visita/consulta',{'msg': 'Registro realizado exitosamente'})
    else:
        return render(request, 'visita.html', {'msg': 'No se puede realizar el registro'})

def consultaVisita(request):
    registro = models.visita.objects.all()
    return render(request,'consultaVisita.html',{"registro":registro})

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

def libroConsulta(request):
    registro = models.libros.objects.all()
    return render(request,'consultaLibro.html',{"registro":registro})

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
    print ("Entro a guardar")
    if 'idPrestamos' in request.POST and 'Isbn' in request.POST and 'Idl' in request.POST and 'fecha' in request.POST and 'Fvencida' in request.POST:
        idPrestamos=request.POST['idPrestamos']
        isbn=request.POST['Isbn']
        Idl=request.POST['Idl']
        fecha=request.POST['fecha']
        Fvencida=request.POST['Fvencida']
        p=models.prestamo(idPrestamos=idPrestamos,isbn_id=isbn,Idl_id=Idl,fecha=fecha,fvencida=Fvencida)
        p.save()
        return render(request, 'Prestamos.html',{'msg':'Registro realizado exitosamente'})
    else:
        return render(request,'Prestamos.html',{'msg':'Registro no se realizo'})

def consultaPrestamos(request):
    registro = models.prestamo.objects.all()
    return render(request,'consultaPrestamos.html',{"registro":registro})

def eliminarP(request):
    if 'idPrestamos' in request.POST:
        per = models.prestamo.objects.get(idPrestamos=request.POST['idPrestamos'])
        per.delete()
    return redirect('/menu/prestamos/consulta')

def Modificacion(request):
    if 'idPrestamos' in request.POST:
        registro = models.prestamo.objects.get(idPrestamos=request.POST['idPrestamos'])
        return render(request,'Modificacion.html',{"reg":registro})
    else:
        return redirect('consulta/')

def modificarP(request):
    if 'idPrestamos' in request.POST and 'Isbn' in request.POST and 'Idl' in request.POST and 'fecha' in request.POST and 'Fvencida' in request.POST:
        p = models.prestamo(idPersona = request.POST['idPrestamos'])
        p.Isbn=request.POST['Isbn']
        p.Idl=request.POST['Idl']
        p.fecha=request.POST['fecha']
        p.Fvencida=request.POST['Fvencida']
        p.save()
    return redirect('consulta', {'mp':'Actualizacion Realizada'})


