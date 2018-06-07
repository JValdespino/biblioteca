# Generated by Django 2.0.5 on 2018-06-07 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lector',
            fields=[
                ('Idl', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=60)),
                ('Edad', models.IntegerField()),
                ('Domicilio', models.CharField(max_length=100)),
                ('Cp', models.CharField(max_length=5)),
                ('Telefono', models.CharField(max_length=12)),
                ('Ocupacion', models.CharField(max_length=50)),
                ('Esc_o_trab', models.CharField(max_length=100)),
                ('Tel_esc', models.CharField(max_length=12)),
                ('Dir_esc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='libros',
            fields=[
                ('isbn', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                ('editorial', models.CharField(max_length=50)),
                ('edicion', models.CharField(max_length=45)),
                ('fimp', models.DateField()),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='prestamo',
            fields=[
                ('idPrestamos', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('fvencida', models.DateField()),
                ('Idl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.lector')),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.libros')),
            ],
        ),
        migrations.CreateModel(
            name='visita',
            fields=[
                ('idVisita', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('fecha', models.DateField()),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]