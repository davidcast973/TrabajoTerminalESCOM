# Generated by Django 2.2.10 on 2020-06-11 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0041_remove_profesor_materias'),
        ('ofertaEducativa', '0010_auto_20200610_2150'),
        ('evaluaciones', '0011_auto_20200506_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestionario',
            name='usuario',
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='UA',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ofertaEducativa.UnidadAprendizaje'),
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='profesorUDA',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Profesor'),
        ),
    ]