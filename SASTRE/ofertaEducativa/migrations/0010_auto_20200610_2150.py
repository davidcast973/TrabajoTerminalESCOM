# Generated by Django 2.2.10 on 2020-06-11 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertaEducativa', '0009_situacionescolar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situacionescolar',
            name='calificacionFinal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='situacionescolar',
            name='extraordinario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='situacionescolar',
            name='primerParcial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='situacionescolar',
            name='segundoParcial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='situacionescolar',
            name='tercerParcial',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]