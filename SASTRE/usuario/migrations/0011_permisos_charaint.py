# Generated by Django 2.2.10 on 2020-02-22 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0010_auto_20200222_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='permisos',
            name='charAint',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]