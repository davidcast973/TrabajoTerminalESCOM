# Generated by Django 2.2.10 on 2020-02-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0016_permisos_charaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='charAint',
        ),
        migrations.AddField(
            model_name='permisos',
            name='charAllllint',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]