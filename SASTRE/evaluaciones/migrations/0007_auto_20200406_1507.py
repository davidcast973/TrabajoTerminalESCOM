# Generated by Django 2.2.10 on 2020-04-06 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluaciones', '0006_cuestionario_materias'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuestionario',
            old_name='materias',
            new_name='preguntas',
        ),
    ]
