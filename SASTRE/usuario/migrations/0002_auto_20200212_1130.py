# Generated by Django 2.2.10 on 2020-02-12 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='promedio',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]