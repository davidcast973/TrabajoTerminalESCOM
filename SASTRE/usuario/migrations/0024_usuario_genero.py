# Generated by Django 2.2.11 on 2020-03-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0023_auto_20200312_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculio')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
