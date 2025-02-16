# Generated by Django 2.2.13 on 2020-06-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcionTesis', '0006_auto_20200616_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesis',
            name='Hola',
        ),
        migrations.AddField(
            model_name='tesis',
            name='abstrac',
            field=models.CharField(default='', max_length=5000, verbose_name='Abstrac de la tesis'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='alumno',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre del alumno autor'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='alumnoAps',
            field=models.CharField(default='', max_length=100, verbose_name='Nombre del alumno autor'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='director1',
            field=models.CharField(default='', max_length=50, verbose_name='Ingresar nombre de director 1'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='director1Aps',
            field=models.CharField(default='', max_length=50, verbose_name='Ingresar nombre de director 1'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='director2',
            field=models.CharField(default='', max_length=50, verbose_name='Ingresar nombre de director 2'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='director2Aps',
            field=models.CharField(default='', max_length=50, verbose_name='Ingresar nombre de director 2'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='nombreTesis',
            field=models.CharField(default='', max_length=500, verbose_name='Titulo de la tesis'),
        ),
        migrations.AddField(
            model_name='tesis',
            name='numeroTesis',
            field=models.IntegerField(default=0),
        ),
    ]
