# Generated by Django 2.2.10 on 2020-02-22 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0014_auto_20200222_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='charAint',
        ),
    ]