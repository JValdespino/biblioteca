# Generated by Django 2.0.5 on 2018-06-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180607_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='idVisita',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
