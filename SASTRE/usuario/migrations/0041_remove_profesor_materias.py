# Generated by Django 2.2.10 on 2020-06-11 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0040_remove_usuario_nombreusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='materias',
        ),
    ]
