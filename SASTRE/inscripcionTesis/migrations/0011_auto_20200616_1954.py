# Generated by Django 2.2.13 on 2020-06-17 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcionTesis', '0010_auto_20200616_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesis',
            name='abstrac',
            field=models.CharField(default='', max_length=5000, null=True, verbose_name='Abstrac de la tesis'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='diaCreacion',
            field=models.DateField(default='1920-01-01', null=True),
        ),
    ]
