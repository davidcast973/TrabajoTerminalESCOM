# Generated by Django 2.2.10 on 2020-02-22 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0009_permisos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisos',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
