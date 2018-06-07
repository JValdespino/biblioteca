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

class consultaInt(models.Model):
    idCon=models.IntegerField(primary_key=True)
    isbn=models.ForeignKey(libros,on_delete=models.CASCADE)
    NombreLe=models.CharField(max_length=50)
    Ap=models.CharField(max_length=50)
    Am=models.CharField(max_length=50)
    Edad=models.IntegerField()
    Tel=models.CharField(max_length=15)
    Dir=models.CharField(max_length=80)
    EscP=models.CharField(max_length=80)

class lector(models.Model):
    Idl = models.AutoField(primary_key=True, auto_created=True)
    Nombre = models.CharField(max_length=60)
    Edad = models.IntegerField()
    Domicilio = models.CharField(max_length=100)
    Cp = models.CharField(max_length=5)
    Telefono = models.CharField(max_length=12)
    Ocupacion = models.CharField(max_length=50)
    Esc_o_trab = models.CharField(max_length=100)
    Tel_esc = models.CharField(max_length=12)
    Dir_esc = models.CharField(max_length=100)

class prestamo(models.Model):
    idPrestamos = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=30)    #Este era un foreignKey
    Idl = models.IntegerField()                #Este era un foreignKey
    fecha = models.DateField()
    fvencida = models.DateField()

class visita(models.Model):
    idVisita = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=80)
    fecha = models.DateField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)