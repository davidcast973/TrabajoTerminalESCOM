# Generated by Django 2.2.10 on 2020-02-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20200218_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.CharField(max_length=10),
        ),
    ]