# Generated by Django 2.2.12 on 2020-05-19 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0040_remove_usuario_nombreusuario'),
        ('inscripcionTesis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='alumno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Alumno'),
        ),
    ]
