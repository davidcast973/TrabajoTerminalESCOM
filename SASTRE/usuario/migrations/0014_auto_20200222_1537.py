# Generated by Django 2.2.10 on 2020-02-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_auto_20200222_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisos',
            name='charAint',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]