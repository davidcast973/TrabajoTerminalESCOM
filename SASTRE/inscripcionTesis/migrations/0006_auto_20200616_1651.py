# Generated by Django 2.2.13 on 2020-06-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcionTesis', '0005_tesis_numerotesis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesis',
            name='abstrac',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='director1',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='director2',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='nombreTesis',
        ),
        migrations.RemoveField(
            model_name='tesis',
            name='numeroTesis',
        ),
        migrations.AddField(
            model_name='tesis',
            name='Hola',
            field=models.CharField(default='PruebaHola', max_length=20),
        ),
    ]
