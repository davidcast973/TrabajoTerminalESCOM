# Generated by Django 2.2.13 on 2020-06-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcionTesis', '0011_auto_20200616_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesis',
            name='valorW2V',
            field=models.FloatField(default=0),
        ),
    ]
