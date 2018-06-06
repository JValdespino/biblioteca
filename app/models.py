from django.db import models

# Create your models here.

class libros(models.Model):
    isbn = models.CharField(max_length=30,primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    edicion = models.CharField(max_length=45)
    fimp = models.DateField()
    tipo = models.CharField(max_length=50)

class prestamos(models.Moddel):
    idPrestamos = models.IntegerField(primary_key=True)
    libros_isbn = models.ForeignKey(libros,on_delete=models.CASCADE)
    lector_Id1 = models.ForeignKey(lector,on_delete=model.CASCADE)
    fecha = models.DateField()
    fvencida = models.DateField()

class visita(model.Moddel):
    idLibro = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=80)
    fecha = models.DateField()
    telefono = IntegerField()
    direccion = CharField(max_length=100)

class lector(models.Moddel):
    Idl = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=60)
    Edad = models.Integer(max_length=11)
    Domicilio = models.CharField(max_length=100)
    Cp = models.CharField(max_length=5)
    Telefono = models.CharField(max_length=12)
    Ocupacion = models.CharField(max_length=50)
    Esc_o_trab = models.CharField(max_length=100)
    Tel_esc = models.CharField(max_length=12)
    Dir_esc = models.CharField(max_length=100)